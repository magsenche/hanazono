import pathlib

import mkdocs.config
from django.conf import settings
from django.http import FileResponse, HttpResponse, JsonResponse
from django.shortcuts import redirect, render

import leitner.quiz
from leitner.models import Flashcard
from utils import logger

config = mkdocs.config.load_config()
docs_dir = pathlib.Path(config["docs_dir"])
log = logger.custom(__name__)


def home(request):
    if request.method == "GET":
        return FileResponse((settings.STATIC_ROOT / "index.html").open("rb"))


def update_flashcard(request, id, is_ok):
    if request.method == "GET":
        is_ok = is_ok.lower() == "true"
        try:
            leitner.quiz.update_flashcard(id, is_ok)
            return JsonResponse({"success": True})
        except Flashcard.DoesNotExist:
            return JsonResponse(
                {"success": False, "error": "Flashcard not found"}, status=404
            )


def daily_quiz(request):
    if request.method == "GET":
        flashcards = Flashcard.objects.all().order_by("?")
        fc_htmls = [fc.html for fc in flashcards if fc.do_quiz()]
        quiz_html = "\n".join(fc_htmls)
        res = render(request, "quiz.html", {"quiz_html": quiz_html})
        quiz_file = settings.STATIC_ROOT / f"notes/quiz/index.html"
        quiz_file.write_text(str(res.content, "utf-8"))
        return redirect(f"/notes/quiz/")


def serve_config(request):
    if request.method == "GET":
        content = f"""
            var HTTP_HOST = "{request.get_host()}";
        """
        return HttpResponse(
            content,
            content_type="application/javascript",
        )


def serve(request, path):
    if request.method == "GET":
        full_path = settings.STATIC_ROOT / path
        if full_path.is_dir():
            full_path = full_path / "index.html"
        if full_path.exists():
            return FileResponse(full_path.open("rb"))
        else:
            return FileResponse((settings.STATIC_ROOT / "404.html").open("rb"))
