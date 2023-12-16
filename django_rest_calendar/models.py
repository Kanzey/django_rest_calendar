from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=30)
    start = models.DateTimeField()
    end= models.DateTimeField()
    location = models.CharField(max_length=256)
    description = models.TextField()
    user = models.DurationField()