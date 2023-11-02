import re

from leitner.models import Flashcard

flashcard_str = """??? question "{question}"
{answer}"""

quiz_flashcard_str = """??? question "{question} {buttons}"
{answer}
    ##### id: {id}, box: {box}, score: {score}, next: {next_review}, last: {last_review}
"""

buttons = "[](){.fbutton .ok}[](){.fbutton .nok}"
flashcard_regex = r"""\?\?\? question "(.*?)".*?\n((?: {4}.*|\n)*?)(?=\n[^\s]|$)"""
definition_regex = r"(`.+`)\n:\s(.+?)(?=\n|$)"


def import_flashcards(markdown_text):
    flashcards = []
    parts = []
    ms = 0
    for m in re.finditer(flashcard_regex, markdown_text):
        parts.append(markdown_text[ms : m.start()])
        ms = m.end()
        flashcard = Flashcard(*m.groups())
        flashcards.append(flashcard)

    parts.append(markdown_text[ms:])
    return flashcards, parts


def import_definitions(markdown_text, file_stem):
    definitions = []
    topic = file_stem.replace("_", " ")
    for m in re.finditer(definition_regex, markdown_text):
        q, d = m.groups()
        question = f"{topic} {q}"
        answer = f"    {d}"
        flashcard = Flashcard(question=question, answer=answer)
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
        )
    else:
        return flashcard_str.format(
            question=flashcard.question, answer=flashcard.answer
        )
