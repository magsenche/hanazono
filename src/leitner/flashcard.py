import hashlib
from dataclasses import dataclass
from datetime import datetime, timedelta


@dataclass
class Flashcard:
    intervals = [0, 1, 6, 14, 30, 66, 150, 360]

    question: str
    answer: str
    id: str = None
    box: int = 1
    next_review: datetime = None
    last_review: datetime = None
    score: dict = None
    buttons: str = "[](){.fbutton .ok}[](){.fbutton .nok}"

    def __post_init__(self):
        if self.id is None:
            self.id = self.generate_flashcard_id()
        if self.next_review is None:
            self.next_review = datetime.now()
        if self.last_review is None:
            self.last_review = datetime.now()
        if self.score is None:
            self.score = {"correct": 0, "incorrect": 0}

    def generate_flashcard_id(self):
        hash_object = hashlib.md5()
        content = self.question + self.answer
        hash_object.update(content.encode("utf-8"))
        return hash_object.hexdigest()[:6]

    def update(self, succes):
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

    def do_quiz(self):
        return self.next_review <= datetime.now()

    def update_score(self, correct=True):
        if correct:
            self.score["correct"] += 1
        else:
            self.score["incorrect"] += 1

    def update_review(self):
        if self.box <= len(self.intervals):
            days_until_next_review = self.intervals[self.box - 1]
        else:
            # After the seventh repetition, maintain the last interval indefinitely
            days_until_next_review = self.intervals[-1]
        self.last_review = datetime.now()
        self.next_review = datetime.now() + timedelta(days=days_until_next_review)
