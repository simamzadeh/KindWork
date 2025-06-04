from django.db import models
from django.contrib.auth.models import User

class Satisfaction(models.Model):
    SATISFACTION_CHOICES = [
        ('very content', 'Very Content'),
        ('content', 'Content'),
        ('neutral', 'Neutral'),
        ('unhappy', 'Unhappy'),
        ('very unhappy', 'Very Unhappy'),
        # Add more mood options here
    ]

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    satisfaction = models.CharField(max_length=50, choices=SATISFACTION_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Satisfaction Log"
        verbose_name_plural = "Satisfaction Logs"

    def __str__(self):
        return f"{self.satisfaction.capitalize()} - {self.user.username} ({self.created_at})"
