from django.db import models
from django.utils import timezone
# Create your models here.

class List(models.Model):
    CATEGORY_CHOICES = [
        ("학교", "school"),
        ("회사", "company"),
        ("가족", "family"),
        ("친구", "friend"),
        ("일과", "daily")
    ]

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default="daily")
    title = models.CharField(max_length=500)
    date_create = models.DateTimeField(default=timezone.now)
    status_delete = models.BooleanField(default=False)
    success = models.IntegerField()

    def __str__(self):
        return self.title