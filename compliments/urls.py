
from django.contrib import admin
from django.urls import include, path

from compliments.views import ComplimentView

urlpatterns = [
    path('compliments.json', ComplimentView.as_view())
]
