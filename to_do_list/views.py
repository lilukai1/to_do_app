from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from to_do_list.models import Task, TaskRelationship, Project
from django.contrib.auth import get_user_model, login
from django.contrib.auth.decorators import login_required
from .forms import (CompletedCheck, AddTaskForm, EditTask, RelationshipInlineFormSet, inlineformset_factory, 
     RelationshipForm) #ProjectForm, ProjectInlineFormSet,
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import RedirectToPreviousMixin
from django.contrib import messages
from datetime import datetime
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.forms import widgets
User = get_user_model()


def base_view(request):
    return render(request, 'base_view.html') 


class AllTasksList(ListView):
    model = Task
    context_object_name = 'task_list'
    paginate_by=10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "All Tasks"    
        context['guest_project'] = Project.objects.get(id=1)
        context['guest_view'] = Task.objects.filter(project=context['guest_project'])
        return context


class ProjectList(ListView):
    model = Project
    context_object_name = 'project_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "All Projects"
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

    def form_valid(self, form):
        form.instance.person = self.request.user
        return super(CreateTaskView, self).form_valid(form)

    def get_success_message(self, cleaned_data):
        return "Task created!"


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
    success_url = '/list_view/'
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
    return HttpResponseRedirect("/list_view/")


# def edit_task_view(request, pk):
#     editing_task = get_object_or_404(Task, pk=pk)
#     success_msg = "Task has been edited!"
#     editing_project = editing_task.get_project()
#     if(editing_task.get_relationships()):
#         relationships = editing_task.get_relationships()
#     add_task_form = AddTaskForm(data=request.POST or None, instance=editing_task, person=person)

#     context={
#         'project' : ProjectInlineFormSet(instance=editing_task),
#         'relationship_form':RelationshipForm(initial={"target_task":"hisss"}),
#         'editing_relationships': editing_task.get_relationships(),
#         'editing_task': editing_task.get_context(),
#         'after_task' :editing_task.get_relationships("after_task"),
#         'before_task' : editing_task.get_relationships("before_task"),
#         "page_title" : f"Editing: { editing_task.title }",
#         }


#     if request.method == 'POST':
#         rel_form = RelationshipInlineFormSet(data=request.POST)
#         project_form = ProjectInlineFormSet(data=request.POST)
#         if add_task_form.is_valid and project_form.is_valid and rel_form.is_valid:
#             saved = add_task_form.save()
#             project_val = post_toasties['current_task-0-project']
#             messages.add_message(request, messages.SUCCESS, success_msg)
#             target_task_val = post_toasties['current_task-0-target_task']

#             ## this sets project
#             if(project_val != ""):     
#                 project = Project.objects.get(id=int(project_val))
#                 adding_project = saved.set_project(project)
#                 messages.add_message(request, messages.SUCCESS, f"Set project to {project.title}")
#             ## this sets relationships for parent/child classes
#             if(target_task_val != ""):            
#                 target = Task.objects.get(id=int(target_task_val))
#                 billy= saved.add_relationship(target, post_toasties['current_task-0-relationship_status'])
#                 messages.success(request, "Added relationship!")
#         return HttpResponseRedirect(saved.get_absolute_url())    




# def add_task_view(request, pk=None):
#     context={}
#     person = request.user

#     editing_task = Task(person=person)
#     editing_project = None
#     success_msg = "Task has been created!"

        
#     post_toasties= request.POST

#     if request.method == 'POST':
#         rel_form = RelationshipInlineFormSet(data=request.POST)
#         project_form = ProjectInlineFormSet(data=request.POST)
#         if add_task_form.is_valid and project_form.is_valid and rel_form.is_valid:
#             saved = add_task_form.save()
#             project_val = post_toasties['current_task-0-project']
#             messages.add_message(request, messages.SUCCESS, success_msg)
#             target_task_val = post_toasties['current_task-0-target_task']

#             ## this sets project
#             if(project_val != ""):     
#                 project = Project.objects.get(id=int(project_val))
#                 adding_project = saved.set_project(project)
#                 messages.add_message(request, messages.SUCCESS, f"Set project to {project.title}")
#             ## this sets relationships for parent/child classes
#             if(target_task_val != ""):            
#                 target = Task.objects.get(id=int(target_task_val))
#                 billy= saved.add_relationship(target, post_toasties['current_task-0-relationship_status'])
#                 messages.success(request, "Added relationship!")
#         return HttpResponseRedirect(saved.get_absolute_url())    

#     else:
#         form_context={
#             'add_task_form': add_task_form,
#             'relationship_form': RelationshipForm(initial={"target_task":"hisss"}),
#             "page_title" : f"Create New Task",
#             # 'project': ProjectInlineFormSet,
#             }
#         context.update(form_context)
#         return render(request, 'add_task_view.html', context=context)



def index_view(request):
    context={            
        "page_title" : f"Create New Task",
    }
    return render(request, 'index_view.html', context)

def base_view(request):
    context={
        "all_tasks": Task.objects.all(),
    }
    return render(request, 'base_view.html', context)


def project_view(request, pk):
    project = get_object_or_404(Project, pk=pk)
    all_project_tasks = TaskRelationship.objects.filter(project_id=pk)
    project_tasks = Task.get_project_tasks(pk)
    progress_bar = 0
    for task in project_tasks:
        if task.completed:
            progress_bar += 1
    context = {
        'project': project,
        "page_title" : f"{project.title}",
        'tasks_completed': TaskRelationship.objects.filter(project_id=pk),
        "project_tasks": project_tasks,
        "progress_bar": len(project_tasks),
        "progress_completed": progress_bar,
    }

    return render(request, 'project_view.html', context) 