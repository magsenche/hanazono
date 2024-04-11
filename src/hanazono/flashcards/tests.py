from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from hanazono.flashcards.models import Flashcard
from hanazono.flashcards.serializers import (
    export_markdown,
    flashcard_str,
    import_flashcards,
)


class FlashcardTestCase(TestCase):
    def setUp(self):
        self.flashcard = Flashcard.objects.create(question="What is 2+2?", answer="4")
        self.flashcard.save()

    def test_generate_flashcard_id(self):
        flashcard1 = Flashcard.objects.create(question="Q1", answer="A1")
        flashcard2 = Flashcard.objects.create(question="Q2", answer="A2")
        self.assertNotEqual(flashcard1.id, flashcard2.id)

    def test_flashcard_quiz(self):
        self.flashcard.next_review = timezone.now() - timezone.timedelta(days=1)
        self.assertTrue(self.flashcard.do_quiz())

        self.flashcard.next_review = timezone.now() + timezone.timedelta(days=1)
        self.assertFalse(self.flashcard.do_quiz())

    def test_flashcard_update(self):
        self.flashcard.update_box(True)
        self.assertEqual(self.flashcard.box, 2)

        for _ in range(5):
            self.flashcard.update_box(True)
        self.flashcard.update_box(False)
        self.assertEqual(self.flashcard.box, 1)

    def test_flashcard_update_score(self):
        initial_correct_score = self.flashcard.score_correct
        self.flashcard.update_score(correct=True)
        self.assertEqual(self.flashcard.score_correct, initial_correct_score + 1)

        initial_incorrect_score = self.flashcard.score_incorrect
        self.flashcard.update_score(correct=False)
        self.assertEqual(self.flashcard.score_incorrect, initial_incorrect_score + 1)

    def test_flashcard_update_review(self):
        initial_next_review = self.flashcard.next_review
        self.flashcard.update_review()
        self.assertNotEqual(self.flashcard.next_review, initial_next_review)


class TestViews(TestCase):
    def setUp(self):
        self.flashcard = Flashcard.objects.create(question="What is 2+2?", answer="4")

    def test_home(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")

    def test_update_flashcard(self):
        url = reverse("update_flashcard", args=(self.flashcard.id, "True"))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["success"], True)
        self.assertEqual(response.json()["box"], 2)

    def test_daily_quiz(self):
        response = self.client.get(reverse("daily_quiz"))
        self.assertEqual(response.status_code, 302)

    def test_serve_config(self):
        response = self.client.get(reverse("serve_config"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["content-type"], "application/javascript")

    def test_serve_nonexistent_file(self):
        response = self.client.get("nonexistent_file.html")
        self.assertEqual(response.status_code, 404)

    def test_update_site(self):
        response = self.client.get(reverse("update_site"))
        self.assertEqual(response.status_code, 302)

    def test_export_data(self):
        response = self.client.get(reverse("export_data"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["content-type"], "application/json")

    def test_import_data(self):
        file_content = b'[{ "model": "flashcards.flashcard", "pk": 1, "fields": { "question": "Test Question", "answer": "Test Answer" } }]'
        uploaded_file = SimpleUploadedFile("test_file.json", file_content)
        initial_count = Flashcard.objects.count()
        response = self.client.post(reverse("import_data"), {"file": uploaded_file})
        self.assertEqual(response.status_code, 302)

        after_import_count = Flashcard.objects.count()
        self.assertEqual(after_import_count, initial_count + 1)

        imported_flashcard = Flashcard.objects.get(question="Test Question")
        self.assertEqual(imported_flashcard.answer, "Test Answer")

    def test_import_invalid_data(self):
        file_content = b"Invalid content"
        uploaded_file = SimpleUploadedFile("invalid_file.json", file_content)
        initial_count = Flashcard.objects.count()
        response = self.client.post(reverse("import_data"), {"file": uploaded_file})
        self.assertEqual(response.status_code, 302)

        after_import_count = Flashcard.objects.count()
        self.assertEqual(after_import_count, initial_count)

    def test_reset_data(self):
        Flashcard.objects.create(question="Q1", answer="A1")
        Flashcard.objects.create(question="Q2", answer="A2")

        response = self.client.get(reverse("reset_data"))
        self.assertEqual(response.status_code, 302)

        reset_count = Flashcard.objects.count()
        self.assertEqual(reset_count, 0)


class FlashcardUtilsTestCase(TestCase):
    def setUp(self):
        self.question = "Check the value of π/2 using python"
        self.answer = """    import math\n    math.cos(math.pi/2) == 0"""

    def test_import_export_consistency(self):
        original_flashcard = Flashcard.objects.create(
            question=self.question, answer=self.answer
        )

        imported_flashcards, _ = import_flashcards(export_markdown(original_flashcard))

        self.assertEqual(len(imported_flashcards), 1)
        imported_flashcard = imported_flashcards[0]
        self.assertEqual(imported_flashcard.question, self.question)
        self.assertEqual(imported_flashcard.answer, self.answer)

    def test_extract_flashcards(self):
        text = (
            "Start of the file\n"
            + flashcard_str.format(question=self.question, answer=self.answer, plus="")
            + "\nSome stuff here\nand here\n"
            + flashcard_str.format(question=self.question, answer=self.answer, plus="")
        )

        extracted_flashcards, _ = import_flashcards(text)

        self.assertEqual(len(extracted_flashcards), 2)
        for extracted_flashcard in extracted_flashcards:
            self.assertEqual(extracted_flashcard.question, self.question)
            self.assertEqual(extracted_flashcard.answer, self.answer)
