from django.urls import include, path
from compliments import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('b', views.compliment_list)
]

urlpatterns = format_suffix_patterns(urlpatterns)
