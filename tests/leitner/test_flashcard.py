from datetime import datetime

import leitner.utils
from leitner.models import Flashcard

id = "a1b2c3"
question = "Check the value of π/2 with python"
answer = """import math\n    math.cos(math.pi/2) == 0"""
box = 1
next_review = datetime.strptime("12/12/2015", "%d/%m/%Y")
last_review = datetime.strptime("10/12/2015", "%d/%m/%Y")
correct, incorrect = 2, 2
score = {"correct": correct, "incorrect": incorrect}

flashcard_md = leitner.utils.flashcard_str.format(question=question, answer=answer)
quiz_flashcard_md = leitner.utils.quiz_flashcard_str.format(
    question=question,
    buttons=leitner.utils.buttons,
    answer=answer,
    id=id,
    box=box,
    score=f"""{score["correct"]}/{score["correct"]+score["incorrect"]}""",
    next_review=next_review.strftime("%d/%m/%Y"),
    last_review=last_review.strftime("%d/%m/%Y"),
)


def test_dbtodb():
    fc = Flashcard(
        question, answer, id, box, next_review, last_review, correct, incorrect
    )
    new_fc = leitner.utils.import_flashcards(leitner.utils.export_markdown(fc))[0][0]

    assert new_fc.question == question
    assert new_fc.answer == answer


def test_mdtomd():
    new_md = leitner.utils.export_markdown(
        leitner.utils.import_flashcards(flashcard_md)[0][0]
    )
    assert flashcard_md == new_md


def test_extract_flashcards():
    text = (
        "Start of the file\n"
        + flashcard_md
        + "\nSome stuff here\nand here\n"
        + flashcard_md
    )
    flashcards, _ = leitner.utils.import_flashcards(text)
    assert leitner.utils.export_markdown(flashcards[0]) == flashcard_md
    assert leitner.utils.export_markdown(flashcards[1]) == flashcard_md


def test_build_quiz():
    fc1 = Flashcard(
        question, answer, id, box, next_review, last_review, correct, incorrect
    )
    quiz_md = "\n".join([leitner.utils.export_markdown(fc, True) for fc in [fc1, fc1]])
    quiz_flashcards, _ = leitner.utils.import_flashcards(quiz_md, True)
    assert quiz_flashcards[0].question == fc1.question
    assert quiz_flashcards[1].question == fc1.question
    assert quiz_flashcards[0].answer == fc1.answer
    assert quiz_flashcards[1].answer == fc1.answer
