from django.db import models
from django.contrib.auth.models import User

class MoodLog(models.Model):
    MOOD_CHOICES = [
        ('very pleasant', 'Very Pleasant'),
        ('pleasant', 'Pleasant'),
        ('neutral', 'Neutral'),
        ('unpleasant', 'Unpleasant'),
        ('very unpleasant', 'Very Unpleasant'),
        # Add more mood options here
    ]

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mood = models.CharField(max_length=50, choices=MOOD_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Mood Log"
        verbose_name_plural = "Mood Logs"

    def __str__(self):
        return f"{self.mood.capitalize()} - {self.user.username} ({self.created_at})"
