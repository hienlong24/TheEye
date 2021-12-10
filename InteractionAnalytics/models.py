from django.db import models


class Event(models.Model):

    session_id = models.CharField(max_length=1000)
    category = models.CharField(max_length=1000)
    name = models.CharField(max_length=1000)
    info = models.JSONField()
    time = models.DateTimeField()


