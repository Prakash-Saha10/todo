from django.db import models
from django.contrib.auth.models import User

class TODO(models.Model):
    serial_number = models.AutoField(primary_key=True)  # More descriptive field name
    title = models.CharField(max_length=100)  # Increased max_length for flexibility
    created_at = models.DateTimeField(auto_now_add=True)  # Renamed for clarity
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title  # Makes it more readable in Django admin and queries
