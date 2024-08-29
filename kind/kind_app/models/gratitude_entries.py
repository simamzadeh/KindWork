from django.db import models
from django.contrib.auth.models import User

class GratitudeEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # class Meta:
    #     ordering = ['-date']

    # def __str__(self):
    #     return f"{self.title} - {self.user.username} ({self.date})"