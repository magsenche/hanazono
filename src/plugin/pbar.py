import re

from bs4 import BeautifulSoup, Tag
from mkdocs.plugins import BasePlugin


class ProgressBarPlugin(BasePlugin):
    def on_post_page(self, output_content, page, config):
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
        new_content = soup.prettify(soup.original_encoding)
        return new_content
