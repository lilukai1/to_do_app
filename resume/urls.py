
from django.contrib import admin
from django.urls import include, path

from resume.views import resume_index, actual_resume, about
# add_task_view,
# from . import views

urlpatterns = [
    path('', resume_index, name='index'),
    path('resume/', actual_resume, name='resume'),
    path('about_me/', about, name='about'),

]
