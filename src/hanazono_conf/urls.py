"""
URL configuration for djangoproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, re_path

from hanazono.flashcards import views

urlpatterns = [
    path("", views.home, name="home"),
    path("admin/update_site/", login_required(views.update_site), name="update_site"),
    path("admin/export_data/", login_required(views.export_data), name="export_data"),
    path("admin/import_data/", login_required(views.import_data), name="import_data"),
    path("admin/reset_data/", login_required(views.reset_data), name="reset_data"),
    path("admin", admin.site.urls),
    path("quiz/", login_required(views.quiz), name="quiz"),
    path(
        "update_flashcard/<str:id>/<str:is_ok>",
        login_required(views.update_flashcard),
        name="update_flashcard",
    ),
    re_path(r"^(?P<path>.*)$", views.serve_mkdocs, name="serve_mkdocs"),
]

if not settings.DEBUG:
    urlpatterns.insert(
        -2, re_path(r"^static/(?P<path>.*)$", views.serve_static, name="serve_static")
    )
