import pathlib

import mkdocs.config
from django.core.management.base import BaseCommand

from leitner.models import Flashcard
from leitner.utils import export_markdown, import_definitions, import_flashcards
from utils import logger

log = logger.custom(__name__)


class Command(BaseCommand):
    help = "Update flashcards."

    def add_arguments(self, parser):
        parser.add_argument("command", choices=["md", "db"])

    def handle(self, *args, **options):
        config = mkdocs.config.load_config()
        notes_dir = pathlib.Path(config["docs_dir"]) / "notes"

        if options["command"] == "md":
            update_markdown(notes_dir)
            log.info("Markdown files updated")
        elif options["command"] == "db":
            update_database(notes_dir)
            log.info("Flashcards database updated")


def update_markdown(docs_dir):
    for mdfile in docs_dir.rglob("*.md"):
        flashcards, parts = import_flashcards(mdfile.read_text())
        new_flashcards = []
        for fc in flashcards:
            try:
                new_flashcard = Flashcard.objects.get(question=fc.question)
                new_flashcards.append(new_flashcard)
            except Flashcard.DoesNotExist:
                new_flashcards.append(fc)
                log.error(f"Error, {fc} not found in database")
        new_flashcard_content = [
            part + export_markdown(fc) for part, fc in zip(parts, new_flashcards)
        ] + [parts[-1]]
        new_md = "".join(new_flashcard_content)

        mdfile.write_text(new_md)


def update_database(docs_dir):
    flashcards_in_md = set()
    for mdfile in docs_dir.rglob("*.md"):
        txt = mdfile.read_text()
        flashcards = import_flashcards(txt)[0]
        flashcards += import_definitions(txt, mdfile.stem)
        for fc in flashcards:
            flashcards_in_md.add(fc.question)
            try:
                flashcard = Flashcard.objects.get(question=fc.question)
            except Flashcard.DoesNotExist:
                flashcard = Flashcard.objects.create(
                    question=fc.question, answer=fc.answer
                )
                log.info(f"Created {flashcard}")
            else:
                if (flashcard.question != fc.question) | (
                    flashcard.answer != fc.answer
                ):
                    log.info(f"Updated {flashcard}")
                    flashcard.question = fc.question
                    flashcard.answer = fc.answer
                    flashcard.save()
    for db_flashcard in Flashcard.objects.all():
        if db_flashcard.question not in flashcards_in_md:
            log.info(f"Removed {db_flashcard}")
            db_flashcard.delete()
