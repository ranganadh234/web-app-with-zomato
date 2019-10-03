from django.db import models
from datetime import datetime
class Bookings(models.Model):
    fullname=models.CharField(max_length=255)
    datetime=models.DateTimeField(default=datetime.now(),blank=True)
    guests=models.IntegerField(blank=True)

    def __str__(self):
        return self.fullname
