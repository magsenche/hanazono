# Generated by Django 5.0.4 on 2024-05-29 11:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("flashcards", "0004_flashcard_file_path_flashcard_hidden"),
    ]

    operations = [
        migrations.CreateModel(
            name="Note",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("filepath", models.TextField(default="")),
                ("content", models.TextField(null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name="flashcard",
            name="file_path",
        ),
        migrations.AddField(
            model_name="flashcard",
            name="note",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="flashcards",
                to="flashcards.note",
            ),
        ),
    ]
