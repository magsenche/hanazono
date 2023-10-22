import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoproject.settings")
django.setup()

import argparse
import pathlib

import mkdocs.config

from leitner.models import Flashcard
from leitner.utils import export_markdown, import_flashcards
from utils import logger

log = logger.custom(__name__)


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
    for mdfile in docs_dir.rglob("*.md"):
        txt = mdfile.read_text()
        flashcards = import_flashcards(txt)[0]
        for fc in flashcards:
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


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Update flashcards.")
    parser.add_argument("command", choices=["md", "db"])
    args = parser.parse_args()
    config = mkdocs.config.load_config()
    notes_dir = pathlib.Path(config["docs_dir"]) / "notes"
    if args.command == "md":
        update_markdown(notes_dir)
        log.info("markdown files updated")
    elif args.command == "db":
        update_database(notes_dir)
        log.info("flashcards database updated")
