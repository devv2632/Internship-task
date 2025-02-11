from django.db import models

class Task(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("completed", "Completed")
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pending")

    def __str__(self):
        return self.title
    
