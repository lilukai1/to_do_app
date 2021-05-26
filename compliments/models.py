from django.db import models
import datetime

from django.db.models.fields import CharField

NATE = 1
ANNIE = 0

PERSON_CHOICES = [
    (NATE, "Nate"),
    (ANNIE, "Annie"),
]

ANYTIME = 0
MORNING = 1
AFTERNOON = 2
EVENING = 3

TIME_CHOICES = [
    (ANYTIME, 'Anytime'),
    (MORNING, 'Morning'),
    (AFTERNOON, 'Afternoon'),
    (EVENING, 'Evening')
]

class Compliments(models.Model):
    compliment = CharField(max_length=75)
    person = models.CharField(max_length=10)
    category = models.IntegerField(choices=TIME_CHOICES, default=ANYTIME)