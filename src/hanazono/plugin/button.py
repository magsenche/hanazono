from bs4 import BeautifulSoup, Tag
from mkdocs.config import config_options
from mkdocs.config.defaults import MkDocsConfig
from mkdocs.plugins import BasePlugin
from mkdocs.structure.pages import Page

from hanazono.utils import logger

log = logger.custom(__name__)


class ButtonPlugin(BasePlugin):
    config_scheme = (("buttons", config_options.Type(list, default=[])),)

    def on_post_page(
        self, output_content: str, page: Page, config: MkDocsConfig
    ) -> str:
        soup = BeautifulSoup(output_content, "html.parser")
        for btn_details in self.config["buttons"]:
            section_class = soup.find("div", {"class": btn_details["class"]})
            if section_class:
                button_element = self._generate_button(btn_details)
                section_class.insert_after(button_element)

        return str(soup)

    def _generate_button(self, details: dict) -> Tag:
        button = Tag(name="a", attrs={"class": "custombutton", "href": details["link"]})
        if "text" in details:
            button.append(details["text"])

        return button
