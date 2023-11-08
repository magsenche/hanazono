import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoproject.settings")
django.setup()

import argparse
import pathlib
import random
import subprocess

import mkdocs.config
import requests

import leitner.utils
from utils import logger

log = logger.custom(__name__)

content_str = leitner.utils.flashcard_str.format(
    question="your question", answer="    answer\n\n-------\n\n{content}"
)


def generate_flashcard(content):
    fc = None
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "testme", "prompt": content, "stream": False},
    )
    if response.status_code == 200:
        response_data = response.json()
        if response_data.get("done", False):
            output = response_data.get("response")
            try:
                log.info(output)
                do_edit = True
                while do_edit:
                    do_edit = ask("Edit flashcard? (y/n): ")
                    if do_edit:
                        content = content_str.format(content=output)
                        new_content = edit(content)
                        fc = leitner.utils.import_flashcards(new_content)[0][0]
                        log.info(f"Q: {fc.question}")
                        log.info(f"A: {fc.answer}")
                        create = ask("Create flashcard? (y/n): ")
                        if create:
                            fc.save()
                            log.info(f"Created {fc}")
                            do_edit = False
            except Exception as e:
                log.error(f"Failed to generate flashcard: {e}")
    return fc


def ask(prompt="(y/n)"):
    while True:
        response = input(prompt).strip().lower()
        if response in ("y", "n"):
            return response == "y"
        else:
            log.info("Invalid input. Enter 'y' for yes, 'n' for no")


def edit(content):
    tmp_file = pathlib.Path("tmp_flashcard.md")
    tmp_file.write_text(content)

    subprocess.run(["vscode", "--wait", "tmp_flashcard.md"])

    new_content = tmp_file.read_text()
    tmp_file.unlink()

    return new_content


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate new flashcards.")
    parser.add_argument("-t", "--topic", type=str, default="")
    parser.add_argument("-n", type=int, default=1)
    args = parser.parse_args()

    config = mkdocs.config.load_config()
    topic = pathlib.Path(config["docs_dir"]) / "notes" / args.topic

    for _ in range(args.n):
        if topic.is_file():
            mdfile = topic
        elif topic.is_dir():
            mdfile = random.choice([f for f in topic.rglob("*.md")])

        log.info(f"Generating flashcard from {mdfile}")
        txt = mdfile.read_text()
        content = txt.split("## Flashcards")[0]
        flashcard = generate_flashcard(content)
        if flashcard is not None:
            new_md = txt + "\n" + leitner.utils.export_markdown(flashcard)
            mdfile.write_text(new_md)
            log.info(f"Updated {mdfile}")
