import re

from bs4 import BeautifulSoup, Tag
from mkdocs.config.defaults import MkDocsConfig
from mkdocs.plugins import BasePlugin
from mkdocs.structure.pages import Page


class ProgressBarPlugin(BasePlugin):
    def on_post_page(
        self, output_content: str, page: Page, config: MkDocsConfig
    ) -> str:
        soup = BeautifulSoup(output_content, "html.parser")
        pbars = soup.find_all("a", {"class": "pbar"})
        for pbar in pbars:
            width, color = re.findall(r"(\d+)%,(\w+)", pbar.text)[0]
            new_pbar = Tag(
                name="div",
                attrs={
                    "class": "pbar",
                    "style": f"width: {width}%; background-color: {color};",
                },
            )
            pbar.replace_with(new_pbar)
        return str(soup)
