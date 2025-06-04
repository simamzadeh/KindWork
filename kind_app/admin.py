from django.contrib import admin
from kind_app.models.gratitude_entry import GratitudeEntry
from kind_app.models.kind_act import KindAct
from kind_app.models.satisfaction import Satisfaction

@admin.register(GratitudeEntry)
class GratitudeEntryAdmin(admin.ModelAdmin):
    list_display = ("id", "user_id", "content", "created_at", "updated_at")

@admin.register(KindAct)
class KindActAdmin(admin.ModelAdmin):
    list_display = ("id", "user_id", "content", "created_at", "updated_at")

@admin.register(Satisfaction)
class SatisfactionAdmin(admin.ModelAdmin):
    list_display = ("id", "user_id", "satisfaction", "created_at")