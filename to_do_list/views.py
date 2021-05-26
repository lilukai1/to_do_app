from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from to_do_list.models import Task, TaskRelationship, Project
from django.contrib.auth import get_user_model, login
from django.contrib.auth.decorators import login_required
from .forms import (CompletedCheck, AddTaskForm, EditTask, RelationshipInlineFormSet, inlineformset_factory, 
     RelationshipForm, AddProjectForm) #ProjectForm, ProjectInlineFormSet,
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import RedirectToPreviousMixin
from django.contrib import messages
from datetime import datetime
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.forms import widgets
from django.urls import reverse, reverse_lazy
from django.http import JsonResponse
from json import dumps
User = get_user_model()


def base_view(request):
    return render(request, 'to_do/base_view.html') 


class AllTasksList(ListView):
    model = Task
    context_object_name = 'task_list'
    paginate_by=10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['personal_projects'] = Project.objects.filter(person=self.request.user)
        except:
            pass
        context["page_title"] = "All Tasks"    
        context['guest_project'] = Project.objects.get(id=1)
        context['guest_view'] = Task.objects.filter(project=context['guest_project'])
        return context

class ProjectList(ListView):
    model = Project
    context_object_name = 'project_list'

    # def get_list(self):
    #     list_check = Project.objects.get_list_or_404(person=self)
    #     return list_check

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['personal_projects'] = Project.objects.filter(person=self.request.user)
        except:
            pass
        context["page_title"] = "All Projects"
        context['guest_view'] = Project.objects.get(id=1)
        return context


class GuestListView(ListView):
    model = Project
    context_object_name = 'project_list'

    # def get_list(self):
    #     list_check = Project.objects.get_list_or_404(person=self)
    #     return list_check

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "To Do Projects"
        context['guest_view'] = Project.objects.get(id=1)
        return context

class ProjectDetailView(DetailView):
    model = Project
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = f"{kwargs['object'].title} Detail"
        context['project_tasks'] = Task.objects.filter(project=kwargs['object'])
        return context


class DetailTaskView(DetailView):
    model = Task
    context_object_name = 'task'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = f"{kwargs['object'].title} Detail"
        return context


# @login_required(login_url="/accounts/login/")
class CreateTaskView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model=Task
    context_object_name='add_task'
    fields =['title', 'description', 'completed', 
        'time_began', 'priority', 'project',]

    def get_form(self, *args, **kwargs):
        form = super(CreateTaskView, self).get_form(*args, **kwargs)
        form.fields['project'].queryset = (Project.objects.filter(person=self.request.user))
        return form

    def form_valid(self, form):
        form.instance.person = self.request.user
        return super(CreateTaskView, self).form_valid(form)

    def get_success_message(self, cleaned_data):
        return "Task created!"


class CreateProjectView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model=Project
    context_object_name='add_project'
    fields =['title', 'description']

    def form_valid(self, form):
        form.instance.person = self.request.user
        return super(CreateProjectView, self).form_valid(form)

    def get_success_message(self, cleaned_data):
        return "Project created!"


class EditTaskView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model=Task
    context_object_name='edit_task'
    fields =['title', 'description', 'completed', 
        'time_began', 'priority', 'project', ]

    def get_success_message(self, cleaned_data):
        return "Task edited!"


class RelationshipEditView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model=TaskRelationship
    context_object_name='edit_task_relationship'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = f"Editing {kwargs['object'].title} Relationships"
        return context

    def get_success_message(self, cleaned_data):
        return "Task Edited Successfully"

class TaskDeleteView(SuccessMessageMixin, LoginRequiredMixin,DeleteView):
    model=Task
    context_object_name='delete_task'
    success_url = reverse_lazy('list_view')
    def get_success_message(self, cleaned_data):
        return "Task Deleted."

@login_required(login_url="/accounts/login/")
def toggle_checkmark(request, pk):
    task = get_object_or_404(Task, pk=pk)    
    if(task.completed==True):
        task.completed = False
        task.time_ended=None
    else:
        task.completed=True
        task.time_ended=timezone.now()
    task.save()
    return HttpResponseRedirect(reverse("list_view"))


def index_view(request):
    context={            
        "page_title" : f"Create New Task",
    }
    return render(request, 'to_do/index_view.html', context)

def base_view(request):
    context={
        "all_tasks": Task.objects.all(),
    }
    return render(request, 'to_do/base_view.html', context)


def project_view(request, pk):
    project = get_object_or_404(Project, pk=pk)
    all_project_tasks = TaskRelationship.objects.filter(project_id=pk)
    project_tasks = Task.get_project_tasks(pk)
    progress_bar = 0
    for task in project_tasks:
        if task.completed:
            progress_bar += 1
    print(len(project_tasks))
    context = {
        'project': project,
        "page_title" : f"{project.title}",
        'tasks_completed': TaskRelationship.objects.filter(project_id=pk),
        "project_tasks": project_tasks,
        "progress_bar": len(project_tasks),
        "progress_completed": progress_bar,
        "project_empty": len(project_tasks)
            }

    return render(request, 'to_do/project_view.html', context) 

# @login_required(login_url="/accounts/login/")
