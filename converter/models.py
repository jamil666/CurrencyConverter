from django.db import models
from datetime import datetime

class Currency(models.Model):

    USD = models.FloatField(max_length=255)
    EURO = models.FloatField(max_length=255)
    GBP = models.FloatField(max_length=255)
    Date = models.CharField(max_length=255, default=datetime.now())
