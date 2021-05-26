
from django.contrib import admin
from django.urls import include, path

from compliments.views import ComplimentView

urlpatterns = [
    path('', ComplimentView.as_view())
]
