import hashlib
import pathlib

from django.db import models
from django.db.models import Avg, Count
from django.utils import timezone

from hanazono.utils import logger

log = logger.custom(__name__)


class Note(models.Model):
    filepath = models.TextField(default="")
    content = models.TextField(null=True)

    def __str__(self) -> str:
        return f"{self.filepath}"

    def save(self, *args, **kwargs):
        if not self.content:
            self.content = pathlib.Path(self.filepath).read_text()
        super().save(*args, **kwargs)


class FlashcardManager(models.Manager):

    def extract(self, file_path: str) -> list[dict]:
        """extract flashcards (question/answer pairs) from a given markdown file"""
        flashcards = []
        for fc in self.filter(file_path=file_path):
            flashcards.append(fc.to_dict())
        return flashcards

    def by_box(self) -> list[dict]:
        """Sort flashcards by box number"""
        return list(self.values("box").annotate(count=Count("id")))

    def file_stats(self) -> list[dict]:
        """Analyzes your flashcards and provides insightful statistics for each file, including the total number of flashcards and the average box they belong to."""
        return list(
            self.values("file_path").annotate(count=Count("id"), average_box=Avg("box"))
        )


class Flashcard(models.Model):
    intervals = [0, 1, 6, 14, 30, 66, 150, 360]
    question = models.TextField()
    answer = models.TextField()
    hidden = models.BooleanField(default=True)
    note = models.ForeignKey(
        Note, related_name="flashcards", null=True, on_delete=models.CASCADE
    )
    id = models.CharField(max_length=6, primary_key=True, default="000000")
    box = models.IntegerField(default=1)
    next_review = models.DateTimeField(null=True)
    last_review = models.DateTimeField(null=True)
    score_correct = models.IntegerField(default=0)
    score_incorrect = models.IntegerField(default=0)
    html = models.TextField(default="")
    objects = FlashcardManager()

    def __str__(self) -> str:
        return f"Flashcard {self.id}: {self.question}"

    def to_dict(self) -> dict:
        return dict(question=self.question, answer=self.answer)

    def save(self, *args, **kwargs):
        if not self.id or self.id == "000000":
            self.id = self.generate_flashcard_id()
        if not self.next_review:
            self.next_review = timezone.now()
        if not self.last_review:
            self.last_review = timezone.now()
        super().save(*args, **kwargs)

    def generate_flashcard_id(self) -> str:
        hash_object = hashlib.md5()
        content = self.question + self.answer
        hash_object.update(content.encode("utf-8"))
        return hash_object.hexdigest()[:6]

    def do_quiz(self) -> bool:
        return self.next_review.date() <= timezone.now().date()

    def update_box(self, success: bool):
        if success:
            self.success()
        else:
            self.fail()
        self.update_review()

    def success(self):
        self.box += 1
        self.update_score()

    def fail(self):
        self.box = 1
        self.update_score(False)

    def update_score(self, correct: bool = True):
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

    def score(self) -> str:
        return f"{self.score_correct}/{self.score_correct+self.score_incorrect}"
