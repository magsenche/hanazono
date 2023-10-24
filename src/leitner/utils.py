import re

from leitner.models import Flashcard

flashcard_str = """??? question "{question}"
    {answer}

"""
quiz_flashcard_str = """??? question "{question} {buttons}"
    {answer}
    ##### id: {id}, box: {box}, score: {score}, next: {next_review}, last: {last_review}
"""

buttons = "[](){.fbutton .ok}[](){.fbutton .nok}"

regex_variables = {
    "question": r"(.+?)",
    "answer": r"(.+?)",
    "buttons": r"\[\]\(\)\{\.fbutton \.ok\}\[\]\(\)\{\.fbutton \.nok\}",
    "id": r"([0-9a-fA-F]{6})",  # 6-digit hex number
    "box": r"(\d+)",  # any number
    "score": r"(\d+/\d+)",  # number/number format
    "next_review": r"(\d{2}/\d{2}/\d{4})",  # date format dd/mm/yyyy
    "last_review": r"(\d{2}/\d{2}/\d{4})",  # date format dd/mm/yyyy
}


def regex(s):
    template = s.replace("\n", "\\n")
    for char in "#?()[]":
        template = template.replace(char, f"\\{char}")
    for variable, pattern in regex_variables.items():
        template = template.replace("{" + variable + "}", pattern)
    return template


def import_flashcards(markdown_text, from_quiz=False):
    flashcards = []
    parts = []
    ms = 0
    fstr = quiz_flashcard_str if from_quiz else flashcard_str
    for m in re.finditer(regex(fstr), markdown_text, re.DOTALL):
        parts.append(markdown_text[ms : m.start()])
        ms = m.end()
        flashcard = Flashcard(*m.groups())
        flashcards.append(flashcard)

    parts.append(markdown_text[ms:])
    return flashcards, parts


def export_markdown(flashcard, for_quiz=False):
    if for_quiz:
        return quiz_flashcard_str.format(
            question=flashcard.question,
            answer=flashcard.answer,
            buttons=buttons,
            id=flashcard.id,
            box=flashcard.box,
            score=flashcard.score(),
            next_review=flashcard.next_review.strftime("%d/%m/%Y"),
            last_review=flashcard.last_review.strftime("%d/%m/%Y"),
        )
    else:
        return flashcard_str.format(
            question=flashcard.question, answer=flashcard.answer
        )
