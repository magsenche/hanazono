import pathlib

import mkdocs.config
from django.core.management.base import BaseCommand

from hanazono.flashcards.models import Flashcard, Note
from hanazono.flashcards.serializers import import_definitions, import_flashcards
from hanazono.utils import logger

log = logger.custom(__name__)
config = mkdocs.config.load_config()


class Command(BaseCommand):
    help = "Update flashcards."

    def add_arguments(self, parser):
        parser.add_argument("command", choices=["db"])

    def handle(self, *args, **options):
        if options["command"] == "db":
            update_database(pathlib.Path(config["docs_dir"]))
            log.info("Database updated")


def update_database(docs_dir: pathlib.Path):
    flashcards_in_notes = set()
    notes_in_docs = set()
    for mdfile in docs_dir.rglob("*.md"):
        # Update note
        content = mdfile.read_text()
        filepath = str(mdfile.relative_to(config["docs_dir"]))
        try:
            note = Note.objects.get(filepath=filepath)
        except Note.DoesNotExist:
            note = Note.objects.create(filepath=filepath, content=content)
            log.info(f"Created {note}")
        else:
            if note.content != content:
                note.content = content
                note.save()
                log.info(f"Updated content: {note}")
        notes_in_docs.add(filepath)

        # Update flashcards
        flashcards, _ = import_flashcards(note.content)
        flashcards += import_definitions(note.content)
        for fc in flashcards:
            flashcards_in_notes.add(fc.question)
            try:
                flashcard = Flashcard.objects.get(question=fc.question)
            except Flashcard.DoesNotExist:
                flashcard = Flashcard.objects.create(
                    question=fc.question, answer=fc.answer, hidden=fc.hidden, note=note
                )
                log.info(f"Created {flashcard}")
            else:
                if flashcard.answer != fc.answer:
                    flashcard.answer = fc.answer
                    flashcard.save()
                    log.info(f"Updated answer: {flashcard}")
                if flashcard.note != note:
                    flashcard.note = note
                    flashcard.save()
                    log.info(f"Updated note to {flashcard.note}: {flashcard}")
                if flashcard.hidden != fc.hidden:
                    flashcard.hidden = fc.hidden
                    flashcard.save()
                    log.info(f"Updated hidden to {flashcard.hidden}: {flashcard}")

    for db_flashcard in Flashcard.objects.all():
        if db_flashcard.question not in flashcards_in_notes:
            log.info(f"Removed {db_flashcard}")
            db_flashcard.delete()
    for db_note in Note.objects.all():
        if db_note.filepath not in notes_in_docs:
            log.info(f"Removed {db_note}")
            db_note.delete()
