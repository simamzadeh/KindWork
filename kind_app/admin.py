from django.contrib import admin
from kind_app.models.achievement import Achievement
from kind_app.models.kudos import Kudos
from kind_app.models.satisfaction import Satisfaction
from kind_app.models.highlight import Highlight

@admin.register(Kudos)
class KudosAdmin(admin.ModelAdmin):
    list_display = ("id", "user_id", "content", "created_at", "updated_at")

@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ("id", "user_id", "content", "created_at", "updated_at")

@admin.register(Highlight)
class HighlightAdmin(admin.ModelAdmin):
    list_display = ("id", "user_id", "content", "created_at", "updated_at")

@admin.register(Satisfaction)
class SatisfactionAdmin(admin.ModelAdmin):
    list_display = ("id", "user_id", "satisfaction", "created_at")