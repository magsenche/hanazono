import re
from datetime import datetime

from leitner.flashcard import Flashcard

template = """??? question "{question} {buttons}"
    {answer}
    ##### id: {id}, box: {box}, score: {score}, next: {next_review}, last: {last_review}
"""

variable_regex = {
    "question": r"(.+?)",
    "buttons": r"\[\]\(\)\{\.fbutton \.ok\}\[\]\(\)\{\.fbutton \.nok\}",
    "answer": r"(.+?)",
    "id": r"([0-9a-fA-F]{6})",  # 6-digit hex number
    "box": r"(\d+)",  # any number
    "score": r"(\d+/\d+)",  # number/number format
    "next_review": r"(\d{2}/\d{2}/\d{4})",  # date format dd/mm/yyyy
    "last_review": r"(\d{2}/\d{2}/\d{4})",  # date format dd/mm/yyyy
}
regex = template.replace("\n", "\\n")
for char in "#?()[]":
    regex = regex.replace(char, f"\\{char}")
for variable, pattern in variable_regex.items():
    regex = regex.replace("{" + variable + "}", pattern)


def find_flashcard_by_id(flashcards, id):
    for fc in flashcards:
        if fc.id == id:
            return fc
    return None


def get_new_md(flashcards, parts):
    new_flashcard_content = [
        part + export_markdown(fc) for part, fc in zip(parts, flashcards)
    ] + [parts[-1]]
    return "".join(new_flashcard_content)


def import_flashcards(markdown_text):
    flashcards = []
    parts = []
    ms = 0

    for m in re.finditer(regex, markdown_text, re.DOTALL):
        parts.append(markdown_text[ms : m.start()])
        ms = m.end()

        question, answer, id, box, score, next, last = m.groups()
        box = int(box)
        correct, total = map(int, score.split("/"))
        score = {
            "correct": correct,
            "incorrect": total - correct,
        }
        next_review = datetime.strptime(next, "%d/%m/%Y")
        last_review = datetime.strptime(last, "%d/%m/%Y")
        flashcards.append(
            Flashcard(question, answer, id, box, next_review, last_review, score)
        )
    parts.append(markdown_text[ms:])
    return flashcards, parts


def export_markdown(flashcard):
    return template.format(
        question=flashcard.question,
        buttons=flashcard.buttons,
        answer=flashcard.answer,
        id=flashcard.id,
        box=flashcard.box,
        score=f"""{flashcard.score["correct"]}/{flashcard.score["correct"]+flashcard.score["incorrect"]}""",
        next_review=flashcard.next_review.strftime("%d/%m/%Y"),
        last_review=flashcard.last_review.strftime("%d/%m/%Y"),
    )
