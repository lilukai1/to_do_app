from .models import Task, Project
from django.contrib.auth import get_user_model

def all_context(request):
    all_context = {"all_tasks": Task.objects.all(),
                    "all_projects": Project.objects.all(),

               }
    return all_context
