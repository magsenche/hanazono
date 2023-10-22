import hashlib

from django.db import models
from django.utils import timezone

from utils import logger

log = logger.custom(__name__)


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

    def generate_flashcard_id(self):
        hash_object = hashlib.md5()
        content = self.question + self.answer
        hash_object.update(content.encode("utf-8"))
        return hash_object.hexdigest()[:6]

    def do_quiz(self):
        return self.next_review.date() < timezone.now().date()

    def update_box(self, succes):
        if succes:
            self.succes()
        else:
            self.fail()
        self.update_review()

    def succes(self):
        self.box += 1
        self.update_score()

    def fail(self):
        self.box = 1
        self.update_score(False)

    def update_score(self, correct=True):
        if correct:
            self.score_correct += 1
        else:
            self.score_incorrect += 1

    def update_review(self):
        if self.box <= len(self.intervals):
            days_until_next_review = self.intervals[self.box - 1]
        else:
            # After the seventh repetition, maintain the last interval indefinitely
            days_until_next_review = self.intervals[-1]
        self.last_review = timezone.now()
        self.next_review = timezone.now() + timezone.timedelta(
            days=days_until_next_review
        )
