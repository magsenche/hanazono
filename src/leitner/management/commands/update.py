import pathlib

import mkdocs.config
from django.core.management.base import BaseCommand

from leitner.models import Flashcard
from leitner.utils import import_definitions, import_flashcards
from utils import logger

log = logger.custom(__name__)
config = mkdocs.config.load_config()


class Command(BaseCommand):
    help = "Update flashcards."

    def add_arguments(self, parser):
        parser.add_argument("command", choices=["db"])

    def handle(self, *args, **options):
        if options["command"] == "db":
            update_database(pathlib.Path(config["docs_dir"]))
            log.info("Flashcards database updated")


def update_database(docs_dir):
    flashcards_in_md = set()
    for mdfile in docs_dir.rglob("*.md"):
        md_txt = mdfile.read_text()
        flashcards, _ = import_flashcards(md_txt)
        flashcards += import_definitions(md_txt)
        for fc in flashcards:
            flashcards_in_md.add(fc.question)
            try:
                flashcard = Flashcard.objects.get(question=fc.question)
            except Flashcard.DoesNotExist:
                flashcard = Flashcard.objects.create(
                    question=fc.question,
                    answer=fc.answer,
                    hidden=fc.hidden,
                    file_path=mdfile.relative_to(config["docs_dir"]),
                )
                log.info(f"Created {flashcard}")
            else:
                if flashcard.answer != fc.answer:
                    flashcard.answer = fc.answer
                    flashcard.save()
                    log.info(f"Updated answer: {flashcard}")
                if flashcard.file_path == "":
                    flashcard.file_path = mdfile.relative_to(config["docs_dir"])
                    flashcard.save()
                    log.info(f"Updated file path to {flashcard.file_path}: {flashcard}")
                if flashcard.hidden != fc.hidden:
                    flashcard.hidden = fc.hidden
                    flashcard.save()
                    log.info(f"Updated hidden to {flashcard.hidden}: {flashcard}")

    for db_flashcard in Flashcard.objects.all():
        if db_flashcard.question not in flashcards_in_md:
            log.info(f"Removed {db_flashcard}")
            db_flashcard.delete()
