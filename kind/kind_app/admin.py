from django.contrib import admin
from kind_app.models.gratitude_entries import GratitudeEntry

@admin.register(GratitudeEntry)
class GratitudeEntryAdmin(admin.ModelAdmin):
    list_display = ("user", "date", "title", "description", "created_at", "updated_at")