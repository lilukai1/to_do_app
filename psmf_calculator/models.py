from django.db import models
import datetime
from django.contrib.auth import get_user_model

SEDENTARY = 1
AEROBIC = 2
WEIGHTS = 3

ACTIVITY_CHOICES = [
    (SEDENTARY, "sedentary"),
    (AEROBIC, "aerobic"),
    (WEIGHTS, "weights"),
]

MALE = 1
FEMALE = 0

GENDER_CHOICES = [
    (MALE, "male"),
    (FEMALE, "female"),
]

class Stats(models.Model):
    age = models.IntegerField()
    weight = models.FloatField()
    height = models.IntegerField()
    #TODO: default birthday of 18 years ago
    # birthday = models.DateField()
    activity = models.IntegerField(choices=ACTIVITY_CHOICES, default=SEDENTARY)
    timestamp = models.DateTimeField(default=datetime.datetime.now)
    person = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    gender = models.IntegerField(choices=GENDER_CHOICES, default=FEMALE)

    def __str__(self):
        return f"{self.person} : {self.weight} lbs"

    def get_bmi(self):
        #Weight (LBS) x 703 ÷ Height (Inches²) 
        return ((self.weight*703)/(self.height*self.height))

    def get_bodyfat(self):
        # bodyfat_lbs = 1.39 * BMI + .16*AGE) - (10.34*gender) -- from wikipedia supposedly more accurate
        # (1.20 x BMI) + (0.23 x Age) – (10.8 x gender) – 5.4 using gender male= 1, female= 0.
        # return ((1.2*bmi) + (.23*age) - (10.8*gender))
        return ((1.39*self.get_bmi() + (.16*self.age)) - (10.34*self.gender))

    
    def get_lbm(self):
        fat_lbs = self.weight * (self.get_bodyfat()/100)
        return (self.weight - fat_lbs)


    def get_category(self):
        if self.gender == 0:
            if self.get_bodyfat() >= .35:
                return 3
            elif self.get_bodyfat() <= .24:
                return 1
            else:
                return 2
        else:
            if self.get_bodyfat() >= .26:
                return 3
            elif self.get_bodyfat() <= .15:
                return 1
            else:
                return 2

    def get_protein_per_lb(self):
        if self.get_category() == 1:
            if self.activity == 1:
                return 1.25
            elif self.activity == 2:
                return 1.5
            else:
                return 2
        if self.get_category() == 2:
            if self.activity == 1:
                return .9
            elif self.activity == 2:
                return 1.1
            else:
                return 1.25
        if self.get_category() == 3:
            if self.activity == 1:
                return .8
            elif self.activity == 2:
                return .9
            else:
                return 1.0


    def get_protein_per_day(self):
        return self.get_lbm() * self.get_protein_per_lb()


class Measurements(models.Model):
    neck = models.DecimalField(max_digits=4, decimal_places=2)
    arm = models.DecimalField(max_digits=4, decimal_places=2)
    wrist = models.DecimalField(max_digits=4, decimal_places=2)
    waist = models.DecimalField(max_digits=4, decimal_places=2)
    hip = models.DecimalField(max_digits=4, decimal_places=2)
    thigh = models.DecimalField(max_digits=4, decimal_places=2)
    calf = models.DecimalField(max_digits=4, decimal_places=2)
    person = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=datetime.datetime.now)


