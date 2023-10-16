import logging
import pathlib
import random
import urllib.parse

from mkdocs.livereload import LiveReloadServer
from mkdocs.plugins import BasePlugin

import leitner

log = logging.getLogger(__name__)


class CustomServer(BasePlugin):
    def on_serve(self, server, config, builder):
        server._serve_request = get_custom_serve_request(server, config)
        return server


def get_custom_serve_request(server, config):
    docs_dir = pathlib.Path(config["docs_dir"])

    def custom_serve_request(environ, start_response):
        res = LiveReloadServer._serve_request(server, environ, start_response)
        if not res:
            if environ["REQUEST_METHOD"] == "GET":
                res = serve_get_request(environ, start_response)
            if environ["REQUEST_METHOD"] == "POST":
                res = serve_post_request(environ, start_response, docs_dir)
        return res

    return custom_serve_request


def serve_get_request(environ, start_response):
    res = None
    if environ["PATH_INFO"] == "/server_config.js":
        content = f"""
            var HTTP_HOST = "{environ["HTTP_HOST"]}";
        """
        start_response(
            "200 OK",
            [
                ("Content-Type", "application/javascript"),
                ("Access-Control-Allow-Origin", "*"),
            ],
        )
        res = [content.encode()]
    return res


def serve_post_request(environ, start_response, docs_dir):
    res = None
    content_length = int(environ.get("CONTENT_LENGTH", "0"))
    post_data = environ["wsgi.input"].read(content_length).decode("utf-8")
    if environ["PATH_INFO"] == "/update_markdown":
        data = urllib.parse.parse_qs(post_data)
        id = data.get("id", [""])[0]
        is_ok = data.get("is_ok", [""])[0] == "true"
        update_markdown(id, is_ok, docs_dir)
        start_response("200 OK", [("Access-Control-Allow-Origin", "*")])
        res = []
    elif environ["PATH_INFO"] == "/generate_quiz":
        generate_quiz(docs_dir)
        start_response("200 OK", [("Access-Control-Allow-Origin", "*")])
        res = []
    return res


def update_markdown(id, is_ok, docs_dir):
    for mdfile in docs_dir.rglob("*.md"):
        if mdfile.stem != "quiz":
            flashcards, parts = leitner.import_flashcards(mdfile.read_text())
            flashcard_to_update = leitner.find_flashcard_by_id(flashcards, id)
            if flashcard_to_update:
                flashcard_to_update.update(is_ok)
                new_md = leitner.get_new_md(flashcards, parts)
                mdfile.write_text(new_md)


def generate_quiz(docs_dir):
    header = "---\nsearch:\n  exclude: true\n---\n"
    title = "# Quiz [⟳](){.qbutton}\n\n"
    body = "## **No flashcard to learn today !**"

    flashcards = []
    for mdfile in docs_dir.rglob("*.md"):
        if mdfile.stem != "quiz":
            txt = mdfile.read_text()
            flashcards += leitner.import_flashcards(txt)[0]
    if len(flashcards) > 0:
        random.shuffle(flashcards)
        to_ask = [fc for fc in flashcards if fc.do_quiz()]
        body = "\n".join([leitner.export_markdown(fc) for fc in to_ask])

    quiz_file = docs_dir / "notes" / "quiz.md"
    with quiz_file.open("w") as f:
        f.write(header + title + body)
