from django.urls import include, path
from compliments import views

urlpatterns = [
    path('', views.compliment_list)
]
