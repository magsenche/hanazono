from datetime import datetime

import leitner

id = "a1b2c3"
question = "Check the value of π/2 with python"
answer = """import math\n    math.cos(math.pi/2) == 0"""
box = 1
next_review = datetime.strptime("12/12/2015", "%d/%m/%Y")
last_review = datetime.strptime("10/12/2015", "%d/%m/%Y")
correct, incorrect = 2, 2
score = {"correct": correct, "incorrect": incorrect}

md_block = leitner.template.format(
    question=question,
    buttons=leitner.Flashcard.buttons,
    answer=answer,
    id=id,
    box=box,
    score=f"""{score["correct"]}/{score["correct"]+score["incorrect"]}""",
    next_review=next_review.strftime("%d/%m/%Y"),
    last_review=last_review.strftime("%d/%m/%Y"),
)


def test_pyparsing():
    fc = leitner.Flashcard(
        question,
        answer,
        id,
        box,
        next_review,
        last_review,
        score,
    )
    new_fc = leitner.import_flashcards(leitner.export_markdown(fc))[0][0]

    assert new_fc.question == question
    assert new_fc.answer == answer
    assert new_fc.id == id
    assert new_fc.box == box
    assert new_fc.next_review == next_review
    assert new_fc.last_review == last_review
    assert new_fc.score == score


def test_mdparsing():
    new_block = leitner.export_markdown(leitner.import_flashcards(md_block)[0][0])
    assert md_block == new_block


def test_extractblock():
    text = (
        "Start of the file\n"
        + md_block
        + "\nSome stuff here\nand here\n"
        + md_block
        + "\nThis is the end"
    )
    flashcards, _ = leitner.import_flashcards(text)
    assert leitner.export_markdown(flashcards[0]) == md_block
    assert leitner.export_markdown(flashcards[1]) == md_block
