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
from django.contrib import admin
from django.urls import path

from leitner import views

urlpatterns = [
    path("", views.home, name="home"),
    path("admin", admin.site.urls),
    path("daily_quiz", views.daily_quiz, name="daily_quiz"),
    path(
        "update_flashcard/<str:id>/<str:is_ok>",
        views.update_flashcard,
        name="update_flashcard",
    ),
    path("server_config.js", views.serve_config, name="serve_config"),
    path("<path:path>", views.serve, name="custom_serve"),
]
