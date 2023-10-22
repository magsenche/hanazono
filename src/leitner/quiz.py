from leitner.models import Flashcard
from utils import logger

log = logger.custom(__name__)


def update_flashcard(id, is_ok):
    flashcard = Flashcard.objects.get(id=id)
    flashcard.update_box(is_ok)
    flashcard.save()
