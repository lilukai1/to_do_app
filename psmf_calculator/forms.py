from django import forms 
from .models import Stats, Measurements
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from datetime import datetime
import requests
from django.forms import inlineformset_factory, BaseInlineFormSet
User= get_user_model()


class AddStatsForm(forms.ModelForm):
    class Meta:
        model = Stats
        fields = ['age', 'weight', 'height', 'activity', 'gender', 'birthday']

    def __init__(self, *args, **kwargs):
        person = kwargs.pop('person')
        self.person = person
        super(AddTaskForm, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.instance.person = self.person
        task = super(AddTaskForm, self).save(*args, **kwargs)
        return task

    def clean(self):
        person = self.person
        self.cleaned_data.update({'person':person})
   

class UpdateStatsForm(forms.ModelForm):
    class Meta:
        model = Stats
        fields = ['weight', 'activity']

    def save(self, *args, **kwargs):
        self.instance.person = self.person
        task = super(AddTaskForm, self).save(*args, **kwargs)
        return task