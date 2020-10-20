
from django.contrib import admin
from django.urls import include, path

from to_do_list.views import (AllTasksList, DetailTaskView, 
                              RelationshipEditView, TaskDeleteView, add_task_view,
                              toggle_checkmark, index_view)

from . import views

urlpatterns = [
    path('', index_view, name='index'),
    path('list_view/', AllTasksList.as_view(template_name='list_view.html'), name='list_view'),
    path('add_task/', add_task_view, name='add_task'),


    path('tasks/', AllTasksList.as_view(template_name="list_view.html"), name ='tasks'),
    path('tasks/<int:pk>/', DetailTaskView.as_view(template_name="detail_view.html"), name ='task_item'),
    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(template_name="delete_view.html"), name='delete_task'),
    path('tasks/<int:pk>/edit_task/', add_task_view, name='edit_task'),
    path('tasks/<int:pk>/toggle_checkmark', toggle_checkmark, name='toggle_checkmark'),
    path('tasks/<int:pk>/relationship/', RelationshipEditView.as_view(template_name="task_entry_view.html"), name='edit_relationship'),

]
