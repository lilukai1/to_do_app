from django.db import models
import datetime

from django.db.models.fields import CharField
from django.db.models.query_utils import Q

NATE = 'Nate'
ANNIE = 'Annie'

PERSON_CHOICES = [
    (NATE, "Nate"),
    (ANNIE, "Annie"),
]

ANYTIME = 'anytime'
MORNING = 'morning'
AFTERNOON = 'afternoon'
EVENING = 'evening'
TIME_CHOICES = [
    (ANYTIME, 'Anytime'),
    (MORNING, 'Morning'),
    (AFTERNOON, 'Afternoon'),
    (EVENING, 'Evening')
]

class PostObject(models.Manager):
    def get_queryset(self):
        question = super().get_queryset().filter(category='anytime')
        return question


class Compliments(models.Model):
    compliment = models.CharField(max_length=75)
    person = models.CharField(max_length=10)
    category = models.CharField(choices=TIME_CHOICES, default="anytime", max_length=20)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return(f"{self.compliment} - {self.person} {self.created}")