from django import forms 
from .models import Task, TaskRelationship
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
        fields = ['title', 'time_began', 'priority',]

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

# def get_relationship_choices():
#     query_fetch = Task.objects.filter(completed=False)
#     choices_list = [q for q in query_fetch]
#     relationship_choices={}
#     print(dir(choices_list))
#     for q in choices_list:
#         print(q.target_task)
#         relationship_choices[q.id] = q.target_task.title

#     return relationship_choices
# print(get_relationship_choices())

# get_relationship_choices = Task.objects.filter(completed=False)
# choices = [c for c in get_relationship_choices]
# print(dict(choices))
class RelationshipForm(BaseInlineFormSet):
    
    class Meta:
        model=TaskRelationship
        fields=['target_task', 'relationship_status']
        # form_choices = get_relationship_choices()
        # widgets={
        #     'target_task' : forms.SelectMultiple(form_choices)
        # }
    # def __init__(self, *args, **kwargs):
    #     super(RelationshipForm, self).__init__(*args, **kwargs)
    #     # self.fields['target_task'].queryset = Task.objects.filter(completed=False)
    #     self.fields['target_task']=


RelationshipInlineFormSet = inlineformset_factory(Task, TaskRelationship, fields=('current_task', 'target_task', 'relationship_status',),
        fk_name='current_task', extra=4, formset=RelationshipForm )
#         # field_classes=('target_task',forms.MultipleChoiceField(Task.objects.filter(completed=False)))
#         )
