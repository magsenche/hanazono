# Django

Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design
## Setup

### Start a project
```bash title=""
$ django-admin startproject mysite
```
or
```bash title=""
django-admin startproject mysite .
```

### Run the dev server
```bash title=""
cd mysite
python manage.py runserver
```
or with custom `IP:PORT`
```bash title=""
cd mysite
python manage.py runserver 0.0.0.0:8000
```

### Create an app
```bash title=""
django-admin startapp myapp
```
then register the app
```python title="djangoproject/settings.py"
INSTALLED_APPS = [
    "myapp",
    ...
}
```

### Create a superuser
This user will be able to access the admin interface. Use `--no-input` along with env variables to allow non-interactive creation.

```sh title=".env"
DJANGO_SUPERUSER_USERNAME=user
DJANGO_SUPERUSER_PASSWORD=pwd
DJANGO_SUPERUSER_EMAIL=""
```

```bash title=""
python manage.py createsuperuser --no-input
```

## Components

### Urls
```python title="djangoproject/urls.py"
urlpatterns = [
    path("", views.home, name="home"),
    path("admin/", admin.site.urls),
    path("daily_quiz", views.daily_quiz, name="daily_quiz"),
    path(
        "update_flashcard/<str:id>/<str:is_ok>",
        views.update_flashcard,
        name="update_flashcard",
    ),
    path("server_config.js", views.serve_config, name="serve_config"),
    path("<path:path>", views.serve, name="custom_serve"),
]
```
### Views
```python title="myapp/views.py"
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

def serve(request, path):
    if request.method == "GET":
        full_path = settings.STATIC_ROOT / path
        if full_path.is_dir():
            full_path = full_path / "index.html"
        if full_path.exists():
            return FileResponse(full_path.open("rb"))
        else:
            return FileResponse((settings.STATIC_ROOT / "404.html").open("rb"))

```

you can also render html from existing template
```python title="myapp/views.py"
def daily_quiz(request):
    if request.method == "GET":
        flashcards = Flashcard.objects.all().order_by("?")
        fc_htmls = [fc.html for fc in flashcards if fc.do_quiz()]
        quiz_html = "\n".join(fc_htmls)
        res = render(request, "quiz.html", {"quiz_html": quiz_html})
        quiz_file = settings.STATIC_ROOT / f"notes/quiz/index.html"
        quiz_file.write_text(str(res.content, "utf-8"))
        return redirect(f"/notes/quiz/")
```

### Models
```python title="myapp/models.py"
class Flashcard(models.Model):
    intervals = [0, 1, 6, 14, 30, 66, 150, 360]
    question = models.TextField()
    answer = models.TextField()
    id = models.CharField(max_length=6, primary_key=True, default="000000")
    box = models.IntegerField(default=1)
    next_review = models.DateTimeField(null=True)
    last_review = models.DateTimeField(null=True)
    score_correct = models.IntegerField(default=0)
    score_incorrect = models.IntegerField(default=0)
    html = models.TextField(default="")

    def __str__(self) -> str:
        return f"Flashcard {self.id}: {self.question}"

    def save(self, *args, **kwargs):
        if not self.id or self.id == "000000":
            self.id = self.generate_flashcard_id()
        if not self.next_review:
            self.next_review = timezone.now()
        if not self.last_review:
            self.last_review = timezone.now()
        super().save(*args, **kwargs)
```

when a model is created or update, prepare the changes:
```bash title=""
python manage.py makemigrations Flashcard
```
and then apply them to the database
```bash title=""
python manage.py migrate
```

### Templates
You can use [templates](https://docs.djangoproject.com/en/5.0/ref/templates/) to introduce html in spectific pages

```html title="myapp/templates/quiz.html"
{% extends "flashcard.html" %}
{% block article_content %}
<article class="md-content__inner md-typeset">{{ quiz_html | safe }}</article>
{% endblock %}
```
```html title="flaschard.html"
<-- content -->
<div class="md-content" data-md-component="content">
{% block article_content %}Default content{% endblock %}
</div>
<-- content -->
```

- `quiz_html | safe` will render the content `quiz_html` as html (not text)
- `article_content` is in the base template
- `flaschard.html` folder is in template dirs:
    ```python title="djangoproject/settings.py"
    BASE_DIR = Path(__file__).resolve().parent.parent
    STATIC_ROOT = BASE_DIR / "site"
    ...
    TEMPLATES = [
        {
            ...
            "DIRS": [STATIC_ROOT],
        },
    ]
    ```

Add buttons:

```html title=""
<div>
    <a class="button" href="/admin/update_site">Udpate site</a>
    <a class="button" href="/admin/reset_data">Reset database</a>
    <a class="button" href="/admin/export_data" download>Export database</a>
</div>
```

### Forms
Define custom forms that can be used with templates to customize the site

```python title="myapp/templates/admin/form.py"
from django import forms


class FileUploadForm(forms.Form):
    file = forms.FileField()
```

```html title="myapp/templates/admin/index.html"
{% extends "admin/index.html" %}

{% block content %}
{{ block.super }}
<div>
    <form method="post" enctype="multipart/form-data" action="{% url 'import_data' %}">
        {% csrf_token %}
        <input type="submit" value="Import database" class="button">
        <input name="file" type="file">
    </form>
</div>
{% endblock %}
```

server-side, to use the form:

```python title="myapp/view.py"
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
```

## Code
### Custom command
[Applications can register their own actions with manage.py](https://docs.djangoproject.com/en/5.0/howto/custom-management-commands/) by adding a `management/commands` and creating a file with the command name.

```python title="myapp/management/commands/build.py"
import mkdocs.config
from django.core.management.base import BaseCommand
from mkdocs.commands import build

from utils import logger

log = logger.custom(__name__)

class Command(BaseCommand):
    help = "Build site."

    def handle(self, *args, **options):
        config = mkdocs.config.load_config()
        build.build(config)
        log.info(f"""Site built in {config["site_dir"]}""")
```

### Database client
Use the `dbshell` command to launch the database client

## Ressources
### Django documentation
- [Djangoproject](https://www.djangoproject.com/)
- [Tutorials](https://docs.djangoproject.com/en/4.2/intro/) with 8 parts

## Flashcards