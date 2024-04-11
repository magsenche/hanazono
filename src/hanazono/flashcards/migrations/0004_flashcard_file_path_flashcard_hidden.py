# Generated by Django 5.0 on 2024-04-11 14:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("flashcards", "0003_remove_flashcard_buttons"),
    ]

    operations = [
        migrations.AddField(
            model_name="flashcard",
            name="file_path",
            field=models.TextField(default=""),
        ),
        migrations.AddField(
            model_name="flashcard",
            name="hidden",
            field=models.BooleanField(default=True),
        ),
    ]
