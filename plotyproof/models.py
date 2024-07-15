
from django.db import models

class DataEntry(models.Model):
    x = models.FloatField()
    y = models.FloatField()
    z = models.FloatField()
