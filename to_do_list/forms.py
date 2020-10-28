from django import forms 
from .models import Task, TaskRelationship, Project
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from datetime import datetime
import requests
from django.forms import inlineformset_factory, BaseInlineFormSet
User= get_user_model()

class CompletedCheck(forms.ModelForm): 

    class Meta: 
        model = Task 
        fields = ['completed']

class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'time_began', 'priority', 'project']

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
        fields = ['title', 'time_began', 'time_ended', 'completed', 'relationships', 'project']

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

# class RelationshipForm(forms.ModelForm):
#     task_select = forms.ModelMultipleChoiceField(queryset=None)
#     class Meta:
#         model = TaskRelationship
#         fields= ['current_task', 'target_task', 'relationship_status']

#     def __init__(self, *args, **kwargs):
#         super(RelationshipForm, self).__init__(*args, **kwargs)
#         task_choices = Task.objects.filter(completed=False)
#         self.fields['target_task'].queryset = Task.objects.filter(completed=False)

        # if not self.instance:



class testadd(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'time_began', 'completed', 'priority',]

    def __init__(self, person, *args, **kwargs):
        super(testadd, self).__init__(*args, **kwargs)
        self.fields['person']=person

def get_relationship_choices():
    query_fetch = Task.objects.filter(completed=False)
    choices_list = [q for q in query_fetch]
    relationship_choices=[]
    for q in choices_list:
        choice = (q.id, q.title)
        relationship_choices.append(choice)
    return relationship_choices


# class ProjectForm(BaseInlineFormSet):

#     class Meta:
#         model=TaskRelationship
#         fields=['project']

class RelationshipForm(forms.ModelForm):

    class Meta:
        model=TaskRelationship
        form_choices = ['before_task','after_task']
        fields=['target_task', 'relationship_status']
     
class AddProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description',]


# ProjectInlineFormSet =  inlineformset_factory(Task, TaskRelationship, fields=('project',),
#     fk_name='current_task', extra=0, can_delete=False)
RelationshipInlineFormSet =  inlineformset_factory(Task, TaskRelationship, fields=('target_task', 'relationship_status'),
    fk_name='current_task', extra=2)