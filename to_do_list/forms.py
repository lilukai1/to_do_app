from django import forms 
from .models import Task, TaskRelationship
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from datetime import datetime
import requests
from django.forms import inlineformset_factory

User= get_user_model()

class CompletedCheck(forms.ModelForm): 

    class Meta: 
        model = Task 
        fields = ['completed']

class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'time_began', 'completed', 'priority',]

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
   
class UpdateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'time_began', 'time_ended', 'completed', 'relationships']

    def save(self, *args, **kwargs):
        self.instance.person = self.person
        task = super(AddTaskForm, self).save(*args, **kwargs)
        return task
    


class EditTask(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['title', 'time_began', 'time_ended', 'completed', 'relationships']


    def save(self, *args, **kwargs):
        tisk = super(EditTask, self).save(commit=False)
        if tisk.completed == True:
            if tisk.time_ended == None:
                tisk.time_ended = datetime.now()
        else:
            tisk.time_ended = None
        tisk.save()
        return tisk

class RelationshipForm(forms.ModelForm):

    class Meta:
        model = TaskRelationship
        fields= ['current_task', 'target_task', 'relationship_status']







class testadd(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'time_began', 'completed', 'priority',]

    def __init__(self, person, *args, **kwargs):
        super(testadd, self).__init__(*args, **kwargs)
        self.fields['person']=person
        
RelationshipInlineFormSet = inlineformset_factory(Task, TaskRelationship, fields=('current_task', 'target_task', 'relationship_status',),
                        fk_name='current_task', extra=2)
