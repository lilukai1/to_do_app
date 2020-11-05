from .models import Task, Project
from django.contrib.auth import get_user_model

projects = Task.objects.all()
all_projects = set([p.project for p in projects])
print(set(all_projects))
def all_context(request):
    all_context = {"all_tasks": Task.objects.all(),
                    "all_projects": set(all_projects),

               }
    return all_context
