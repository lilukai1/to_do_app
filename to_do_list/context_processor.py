from .models import Task
from django.contrib.auth import get_user_model

def all_context(request):
    all_context = {"all_tasks": Task.objects.all(),
               }
    return {"all_tasks": Task.objects.all(),
               }
