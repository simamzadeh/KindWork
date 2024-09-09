from django.contrib import admin
from kind_app.models.gratitude_entry import GratitudeEntry

@admin.register(GratitudeEntry)
class GratitudeEntryAdmin(admin.ModelAdmin):
    list_display = ("id", "user_id", "content", "created_at", "updated_at")