
from django.contrib import admin
from django.urls import include, path

from to_do_list.views import (AllTasksList, DetailTaskView, MassEditView,
                              RelationshipEditView, TaskDeleteView,
                              TaskEditAllView, TaskEditView, add_task_view,
                              toggle_checkmark)

from . import views

urlpatterns = [
    path('', AllTasksList.as_view(template_name='list_view.html'), name='list_view'),
    path('list_view/', AllTasksList.as_view(template_name='list_view.html'), name='list_view'),
    path('tasks/', AllTasksList.as_view(template_name="list_view.html"), name ='tasks'),
    path('tasks/<int:pk>/', DetailTaskView.as_view(template_name="detail_view.html"), name ='task_item'),

    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(template_name="delete_view.html"), name='delete_task'),
    # path('add_task/', TaskEntryView.as_view(template_name="task_entry_view.html"), name='add_task'),
    
    # path('tasks/<int:pk>/edit_task/', TaskEditView.as_view(template_name="add_task_view.html"), name='edit_task'),
    path('tasks/<int:pk>/edit_task/', add_task_view, name='edit_task'),
    path('tasks/<int:pk>/toggle_checkmark', toggle_checkmark, name='toggle_checkmark'),

    path('edit_task/', MassEditView.as_view(template_name="mass_edit_view.html"), name='mass_edit_view'),
    path('tasks/<int:pk>/relationship/', RelationshipEditView.as_view(template_name="task_entry_view.html"), name='edit_relationship'),


    # path('list_view/', views.view_task_detail),
    path('edit_all/', TaskEditAllView.as_view(template_name="mass_edit_view.html")), 


    path('add_task/', add_task_view, name='add_task'),


]
