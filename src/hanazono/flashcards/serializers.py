import re

from hanazono.flashcards.models import Flashcard

flashcard_str = """???{plus} question "{question}"
{answer}"""

quiz_flashcard_str = """??? question "{question} {buttons}"
{answer}
    ##### [note]({file_path}), id: {id}, box: {box}, score: {score}, next: {next_review}, last: {last_review}
"""

buttons = "[](){.fbutton .ok}[](){.fbutton .nok}"
flashcard_regex = r"""\?\?\?(\+?) question "(.*?)".*?\n((?: {4}.*|\n)*?)(?=\n[^\s]|$)"""
definition_regex = r"(`.+`)\n:\s(.+?)(?=\n|$)"


def import_flashcards(markdown_text):
    flashcards = []
    parts = []
    ms = 0
    for m in re.finditer(flashcard_regex, markdown_text):
        parts.append(markdown_text[ms : m.start()])
        ms = m.end()
        plus, question, answer = m.groups()
        hidden = not plus == "+"
        flashcard = Flashcard(question=question, answer=answer, hidden=hidden)
        flashcards.append(flashcard)

    parts.append(markdown_text[ms:])
    return flashcards, parts


def import_definitions(markdown_text):
    definitions = []
    for m in re.finditer(definition_regex, markdown_text):
        q, d = m.groups()
        question = f"{q}"
        answer = f"    {d}"
        flashcard = Flashcard(question=question, answer=answer, hidden=False)
        definitions.append(flashcard)

    return definitions


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
            file_path=flashcard.file_path,
        )
    else:
        plus = "" if flashcard.hidden else "+"
        return flashcard_str.format(
            plus=plus, question=flashcard.question, answer=flashcard.answer
        )
