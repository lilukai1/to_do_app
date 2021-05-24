
from django.contrib import admin
from django.urls import include, path

from to_do_list.views import (AllTasksList, DetailTaskView, base_view, ProjectDetailView,
                              RelationshipEditView, TaskDeleteView, EditTaskView,
                              toggle_checkmark, index_view, ProjectList, CreateTaskView,
                              CreateProjectView)
from . import views

urlpatterns = [
    path('index/', index_view, name='to_do_index'),
    path('tasks/list/', AllTasksList.as_view(template_name='to_do/list_view.html'), name='list_view'),
    path('tasks/add/task/', CreateTaskView.as_view(template_name="to_do/add_task_view.html"), name='add_task'),
    path('tasks/add/project/', CreateProjectView.as_view(template_name="to_do/add_project_view.html"), name='add_project'),

    path('tasks/<int:pk>/', DetailTaskView.as_view(template_name="to_do/detail_view.html"), name ='task_detail'),
    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(template_name="to_do/delete_view.html"), name='delete_task'),
    path('to_do/tasks/<int:pk>/edit_task/', EditTaskView.as_view(template_name="to_do/add_task_view.html"), name='edit_task'),
    path('to_do/tasks/<int:pk>/toggle_checkmark', toggle_checkmark, name='toggle_checkmark'),
    path('to_do/tasks/<int:pk>/relationship/', RelationshipEditView.as_view(template_name="to_do/relationship_view.html"), name='edit_relationship'),

    path('to_do/projects/', ProjectList.as_view(template_name="to_do/project_list_view.html"), name ='projects'),
    path('to_do/projects/<int:pk>/', ProjectDetailView.as_view(template_name='to_do/project_view.html'), name ='project_detail'),

]
