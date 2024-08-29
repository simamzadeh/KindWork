from django.db import models
from django.contrib.auth.models import User

class GratitudeEntry(models.Model):
    entry_id = models.AutoField(primary_key=True)  # New primary key field
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, to_field='id')  # Foreign key referencing user.id
    content = models.TextField()  # Combining title and description into one field
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # class Meta:
    #     ordering = ['-date']

    # def __str__(self):
    #     return f"{self.title} - {self.user.username} ({self.date})"