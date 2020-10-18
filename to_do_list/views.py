from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from to_do_list.models import Task, TaskRelationship
from django.contrib.auth import get_user_model
from .forms import CompletedCheck, AddTaskForm, EditTask, RelationshipForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from datetime import datetime
from .forms import testadd, inlineformset_factory, RelationshipInlineFormSet
from django.http import HttpResponseRedirect

User = get_user_model()

def add_task_view(request):
    return render(request, 'base_view.html')

def base_view(request):
    return render(request, 'base_view.html') 

def view_task_detail(request):
    return render(request, 'base_view.html')

class AllTasksList(ListView):
    model = Task
    context_object_name = 'task_list'

class DetailTaskView(DetailView):
    model = Task
    context_object_name = 'task'

class TaskEntryView(SuccessMessageMixin, CreateView):
    model=Task
    form_class= AddTaskForm
    context_object_name='add_task'
    success_url= '/'

    def get_form_kwargs(self):
        kwargs = super(TaskEntryView, self).get_form_kwargs()
        kwargs.update({'person' : self.request.user})
        return kwargs

    def get_success_message(self, cleaned_data):
        return "Task created!"


class TaskEditView(SuccessMessageMixin, UpdateView):
    model=Task
    form_class= EditTask
    context_object_name='edit_task'
    
    def get_success_message(self, cleaned_data):
        return "Task Edited Successfully"

class RelationshipEditView(SuccessMessageMixin, CreateView):
    model=TaskRelationship
    form_class= RelationshipForm
    context_object_name='edit_task_relationship'
    success_url= '/'
    
    def get_success_message(self, cleaned_data):
        return "Task Edited Successfully"

class TaskDeleteView(SuccessMessageMixin, DeleteView):
    model=Task
    context_object_name='delete_task'
    success_url = '/'
    def get_success_message(self, cleaned_data):
        return "Task Deleted."

class TaskEditAllView(UpdateView):
    model=Task
    form_class= EditTask
    context_object_name='edit_task'

class MassEditView(ListView):
    model = Task
    context_object_name = 'mass_edit'

def toggle_checkmark(request, pk):
    task = get_object_or_404(Task, pk=pk)    
    if(task.completed==True):
        task.completed = False
        task.time_ended=None
    else:
        task.completed=True
        task.time_ended=datetime.now()
    task.save()
    return HttpResponseRedirect("/")



    # checkbox_value = request.POST["task_complete"]
    # checkbox_id = int(request.POST["id_of_element"])
    # task_to_modify = ToDoChecklistTask.objects.get(id = checkbox_id)

    # task_to_modify.task_check_marked = (checkbox_value == "true")
    # task_to_modify.save()

    # data_to_return = serializers.serialize('json', ToDoChecklistTask.objects.all());
    # return HttpResponse(data_to_return, 'application/json')


def add_task_view(request, pk=None):
    context={}
    person = request.user
    RelationshipInlineFormSet = inlineformset_factory(Task, TaskRelationship, 
                            fields=('target_task', 'relationship_status',),
                            fk_name='current_task', extra=1)

    if pk != None:
        editing_task = get_object_or_404(Task, pk=pk)
        success_msg = "Task has been edited!"
        context={
        
        'editing_relationships': editing_task.get_relationships(),
        'editing_task': editing_task.get_context(),
        'after_task' :editing_task.get_relationships("after_task"),
        'before_task' : editing_task.get_relationships("before_task"),
        }

    else:
        editing_task = Task(person=person)
        success_msg = "Task has been created!"

    add_task_form = AddTaskForm(data=request.POST or None, instance=editing_task, person=person)
    post_toasties= request.POST

    print("post toasties", post_toasties)
    print(request.method)
    if request.method == 'POST':
        rel_form = RelationshipInlineFormSet(data=request.POST)
        if add_task_form.is_valid and rel_form.is_valid:
            saved = add_task_form.save()
            messages.add_message(request, messages.SUCCESS, success_msg)
            target_task_val = post_toasties['current_task-0-target_task']

            if(target_task_val != ""):            
                target = Task.objects.get(id=int(post_toasties['current_task-0-target_task']))
                billy= saved.add_relationship(target, post_toasties['current_task-0-relationship_status'])
                messages.success(request, "Added relationship!")
        return HttpResponseRedirect(saved.get_absolute_url())    

    else:
        form_context={
            'add_task_form': add_task_form,
            'relationship_form': RelationshipInlineFormSet,
            }
        context.update(form_context)
        print(context)
        print(editing_task.title)
        return render(request, 'add_task_view.html', context=context)

