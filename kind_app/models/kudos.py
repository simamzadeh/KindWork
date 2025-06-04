from django.db import models
from django.contrib.auth.models import User

class Kudos(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Kudos Entry"
        verbose_name_plural = "Kudos Entries"

    def __str__(self):
        return f"{self.title} - {self.user.username} ({self.date})"