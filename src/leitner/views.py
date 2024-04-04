import pathlib

import mkdocs.config
from django.conf import settings
from django.core.management import call_command
from django.core.serializers import deserialize, serialize
from django.http import FileResponse, Http404, HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.utils import timezone

from leitner.forms import FileUploadForm
from leitner.models import Flashcard
from utils import logger

config = mkdocs.config.load_config()
log = logger.custom(__name__)


def home(request):
    if request.method == "GET":
        return render(request, "index.html")


def update_flashcard(request, id, is_ok):
    if request.method == "GET":
        is_ok = is_ok.lower() == "true"
        try:
            flashcard = Flashcard.objects.get(id=id)
            flashcard.update_box(is_ok)
            flashcard.save()
            return JsonResponse(
                {
                    "success": True,
                    "box": flashcard.box,
                    "next_review_date": flashcard.next_review.date(),
                    "score": flashcard.score(),
                }
            )
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
        quiz_file = settings.STATIC_ROOT / f"quiz/index.html"
        quiz_file.write_text(str(res.content, "utf-8"))
        return redirect(f"/quiz/")


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
            raise Http404(f"path not found: {path} ")


def update_site(request):
    if request.method == "GET":
        try:
            call_command("makemigrations")
            call_command("migrate")
            call_command("update", "db")
            call_command("build")

            log.info("Site updated")
            return redirect(f"home")
        except Exception as e:
            log.error(f"Error updating site: {str(e)}")
            return redirect(f"/admin")


def export_data(request):
    if request.method == "GET":
        try:
            data = serialize("json", Flashcard.objects.all())
            filename = f"flashcards_{timezone.now().strftime('%d%m%y')}.json"
            log.info(f"Data exported successfully")
            return HttpResponse(
                data,
                content_type="application/json",
                headers={"Content-Disposition": f"attachment; filename={filename}"},
            )
        except Exception as e:
            log.error(f"Error exporting data: {str(e)}")
            return redirect(f"/admin")


def import_data(request):
    if request.method == "POST":
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file_obj = form.cleaned_data["file"]
            try:
                flashcards = list(deserialize("json", file_obj))
                for fc in flashcards:
                    fc.object.save()
                    log.info(f"Imported {fc.object}")
                return redirect(f"/admin/update_site/")
            except Exception as e:
                log.error(f"Can't load data from {file_obj.name}: {str(e)}")
                return redirect(f"/admin")


def reset_data(request):
    if request.method == "GET":
        Flashcard.objects.all().delete()
        log.info("Database reseted")
        return redirect(f"/admin")
