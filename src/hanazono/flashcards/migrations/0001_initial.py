# Generated by Django 4.2.6 on 2023-10-17 14:42

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Flashcard",
            fields=[
                ("question", models.TextField()),
                ("answer", models.TextField()),
                (
                    "id",
                    models.CharField(
                        default="000000",
                        max_length=6,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("box", models.IntegerField(default=1)),
                ("next_review", models.DateTimeField(null=True)),
                ("last_review", models.DateTimeField(null=True)),
                ("score_correct", models.IntegerField(default=0)),
                ("score_incorrect", models.IntegerField(default=0)),
                (
                    "buttons",
                    models.TextField(default="[](){.fbutton .ok}[](){.fbutton .nok}"),
                ),
            ],
        ),
    ]