import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoproject.settings")
django.setup()
import pathlib

from bs4 import BeautifulSoup, NavigableString
from mkdocs.config import config_options
from mkdocs.config.defaults import MkDocsConfig
from mkdocs.plugins import BasePlugin
from mkdocs.structure.files import File, Files
from mkdocs.structure.pages import Page

from leitner.models import Flashcard
from leitner.utils import export_markdown
from utils import logger

log = logger.custom(__name__)


class QuizPlugin(BasePlugin):
    config_scheme = (("buttons", config_options.Type(list, default=[])),)

    def __init__(self) -> None:
        super().__init__()
        self.quiz_uri = "notes/quiz.md"
        self.md_file = None
        self.html_file = None
        self.flashcard_html_file = None

    def on_config(self, config: MkDocsConfig) -> MkDocsConfig | None:
        self.md_file = pathlib.Path(config["docs_dir"]) / self.quiz_uri
        self.html_file = (pathlib.Path(config["site_dir"]) / self.quiz_uri).with_suffix(
            ""
        ) / "index.html"
        self.flashcard_html_file = pathlib.Path(config["site_dir"]) / "flashcard.html"
        return config

    def on_files(self, files: Files, *, config: MkDocsConfig) -> Files | None:
        # Write the content of all flashcards to a markdown file to be processed
        md = "\n".join([export_markdown(fc, True) for fc in Flashcard.objects.all()])
        self.md_file.write_text(md)
        files.append(File(self.quiz_uri, config["docs_dir"], config["site_dir"], True))
        return files

    def on_post_page(
        self, output: str, *, page: Page, config: MkDocsConfig
    ) -> str | None:
        if pathlib.Path(page.url).stem == "quiz":
            soup = BeautifulSoup(output, "html.parser")

            # Extract all flashcards html
            for fc in Flashcard.objects.all():
                id_element = soup.find(string=lambda text: "id: " + fc.id in text)
                if id_element:
                    fc_html = id_element.find_parents("details")[0]
                    fc.html = fc_html.prettify(soup.original_encoding)
                    fc.save()

            # Prepare for the quiz template
            article_tag = soup.find("article")
            if article_tag:
                new_content = NavigableString(
                    "{% block article_content %}Default content{% endblock %}"
                )
                article_tag.replace_with(new_content)
            flashcard_html = soup.prettify(soup.original_encoding)
            self.flashcard_html_file.write_text(flashcard_html)

        return output

    def on_post_build(self, *, config: MkDocsConfig) -> None:
        self.md_file.unlink()
        self.html_file.unlink()
