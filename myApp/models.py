from django.db import models

class DateAndTime(models.Model):
    when = models.DateTimeField('Date and Time', auto_now_add=True)

