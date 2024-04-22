import pathlib

from django.contrib import admin
from django.core.management import call_command

from hanazono.flashcards.models import Flashcard, Note


class FlashcardAdmin(admin.ModelAdmin):
    actions = ["export_flashcards"]

    @admin.action(description="Export selected flashcards")
    def export_flashcards(self, request, queryset):
        output_file = pathlib.Path("flahscards.json")
        selected_pks = ",".join(str(obj.pk) for obj in queryset)
        call_command(
            "dumpdata",
            f"flashcards.flashcard",
            output=output_file,
            pks=selected_pks,
        )
        self.message_user(
            request,
            f"Exported flashcards to {output_file.absolute()}: {selected_pks}",
        )


admin.site.register(Flashcard, FlashcardAdmin)
admin.site.register(Note)
