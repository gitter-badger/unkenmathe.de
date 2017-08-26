"""Admin."""
from django.contrib import admin
from .models import Exercise


class ExerciseAdmin(admin.ModelAdmin):
    """Admin interface for the Exercise model."""

    fields = ('author', 'text', 'text_html', 'text_tex')
    readonly_fields = ('text_html', 'text_tex')

    list_display = ('id', 'author')
    list_filter = ('author', )


admin.site.register(Exercise, ExerciseAdmin)