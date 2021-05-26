from django.urls import include, path
from compliments import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('', views.compliment_list),
    path('list', views.compliment_list)

]

urlpatterns = format_suffix_patterns(urlpatterns)
