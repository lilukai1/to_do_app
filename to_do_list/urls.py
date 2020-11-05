
from django.contrib import admin
from django.urls import include, path

from to_do_list.views import (AllTasksList, DetailTaskView, base_view, ProjectDetailView,
                              RelationshipEditView, TaskDeleteView, EditTaskView,
                              toggle_checkmark, index_view, ProjectList, CreateTaskView)
# add_task_view,
from . import views

urlpatterns = [
    path('', index_view, name='index'),
    path('list_view/', AllTasksList.as_view(template_name='list_view.html'), name='list_view'),
    # path('add_task/', add_task_view, name='add_task'),
    path('add/', CreateTaskView.as_view(template_name="add_task_view.html"), name='add_task'),
    path('base/', base_view, name="edit_task"),

    path('tasks/', AllTasksList.as_view(template_name="list_view.html"), name ='tasks'),
    path('tasks/<int:pk>/', DetailTaskView.as_view(template_name="detail_view.html"), name ='task_detail'),
    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(template_name="delete_view.html"), name='delete_task'),
    # path('tasks/<int:pk>/edit_task/', add_task_view, name='edit_task'),

    path('tasks/<int:pk>/edit_task/', EditTaskView.as_view(template_name="add_task_view.html"), name='edit_task'),
    path('tasks/<int:pk>/toggle_checkmark', toggle_checkmark, name='toggle_checkmark'),
    path('tasks/<int:pk>/relationship/', RelationshipEditView.as_view(template_name="relationship_view.html"), name='edit_relationship'),


    path('projects/', ProjectList.as_view(template_name="project_list_view.html"), name ='projects'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(template_name='project_view.html'), name ='project_detail'),



]
