# Generated by Django 4.2.6 on 2023-10-20 08:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("leitner", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="flashcard",
            name="html",
            field=models.TextField(default=""),
        ),
    ]
