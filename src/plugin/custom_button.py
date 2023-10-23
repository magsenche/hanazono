from bs4 import BeautifulSoup, Tag
from mkdocs.config import config_options
from mkdocs.plugins import BasePlugin

from utils import logger

log = logger.custom(__name__)


class CustomButton(BasePlugin):
    config_scheme = (("buttons", config_options.Type(list, default=[])),)

    def on_post_page(self, output_content, page, config):
        soup = BeautifulSoup(output_content, "html.parser")
        for btn_details in self.config["buttons"]:
            section_class = soup.find("div", {"class": btn_details["class"]})
            if section_class:
                button_element = self._generate_button(btn_details)
                section_class.insert_after(button_element)

        souped_html = soup.prettify(soup.original_encoding)
        return souped_html

    def _generate_button(self, details):
        """
        Generate a BeautifulSoup button element based on provided details.
        """
        button = Tag(name="a", attrs={"class": "custombutton", "href": details["link"]})

        # If there's text, add it to the button
        if "text" in details:
            button.append(details["text"])

        return button
