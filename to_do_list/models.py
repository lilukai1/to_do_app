from django.db import models
from django.db.models import Q
from datetime import datetime
from django.utils import timezone

from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse

RELATIONSHIP_AFTER_TASK = 'after_task'
RELATIONSHIP_BEFORE_TASK = 'before_task'
RELATIONSHIP_STATUS = [
    (RELATIONSHIP_AFTER_TASK, 'Current task can be done after '),
    (RELATIONSHIP_BEFORE_TASK, 'Current task must be done before '),
    ]

def opposite_status(status):
    if(status==RELATIONSHIP_AFTER_TASK):
        opposite_status=RELATIONSHIP_BEFORE_TASK
    else:
        opposite_status=RELATIONSHIP_AFTER_TASK
    return opposite_status


class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return(self.title)

    def get_absolute_url(self):
        return reverse('task_detail', kwargs={'pk': self.pk})    

    def get_progress(self):
        tasks = Task.objects.filter(project=self)
        print('ok')
        progress_completed= tasks.completed.count()
        print(progress_completed)
        progress_max= tasks.count()
        print(progress_max)
        print(progress_completed,progress_max)
        return(progress_completed/progress_max)

class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True, related_name="children", related_query_name="kids")
    title = models.CharField(max_length=100)
    description = models.TextField(default="", blank=True, null = True, max_length=200)
    completed = models.BooleanField(default=False)
    person = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,)
    time_began = models.DateTimeField(default=timezone.now)
    time_ended = models.DateTimeField(null=True, blank=True)
    priority = models.IntegerField(default=5 )
    relationships = models.ManyToManyField('self', symmetrical=False, through='TaskRelationship', related_name='related_to')

    def __str__(self):
        return(self.title)

    def get_absolute_url(self):
        return reverse('task_detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['completed','priority', 'title']

    def add_relationship(self, task, status, symm=True):
        relationship, created = TaskRelationship.objects.get_or_create(
            current_task=self,
            target_task=task,
            relationship_status=status)
        reverse_relationship, created = TaskRelationship.objects.get_or_create(
            current_task=task,
            target_task=self,
            relationship_status=opposite_status(status))
        return relationship


    def remove_relationship(self, task, symm=True):
        TaskRelationship.objects.filter(current_task=self, target_task=task).delete()
        TaskRelationship.objects.filter(target_task=self, current_task=task).delete()
        return

## Returns all tasks and project associated with task in question.
    def get_relationships(self, status = None):
        relation_filter = TaskRelationship.objects.filter(Q(current_task_id=self.id) | Q(target_task_id=self.id))
        if status == "before_task":
            relation_filter = TaskRelationship.objects.filter(
                Q(current_task_id=self.id), relationship_status=RELATIONSHIP_BEFORE_TASK)
        elif status == "after_task":
            relation_filter = TaskRelationship.objects.filter(
                Q(current_task_id=self.id), relationship_status=RELATIONSHIP_AFTER_TASK)
        return relation_filter



    def get_context(self):
        context = {
            'title':self.title,
            'id':self.id,
            'time_began':self.time_began,
            'time_ended': self.time_ended,
            'completed' : self.completed,
            'priority' : self.priority,
            'person' : self.person,
            'relationships' : self.get_relationships(),
            'before_tasks' : self.get_relationships('before_task'),
            'after_tasks' : self.get_relationships('after_task'),
        }
        return context



class TaskRelationship(models.Model):
    current_task= models.ForeignKey(Task, related_name="current_task", on_delete=models.CASCADE, )
    target_task = models.ForeignKey(Task, related_name="target_task", on_delete=models.CASCADE, null=True,
                    limit_choices_to={'completed':False})
    relationship_status = models.CharField(max_length=50, choices=RELATIONSHIP_STATUS) 

    def __str__(self):
        return f"{self.current_task.title}'s {self.relationship_status} is {self.target_task}"

    def get_absolute_url(self):
        return reverse('task_detail', kwargs={'pk': self.pk})
        
# register(Task)
