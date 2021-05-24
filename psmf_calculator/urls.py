
from django.contrib import admin
from django.urls import include, path

from psmf_calculator.views import Add_Stats, Stats

urlpatterns = [
    # path('', add_stats, name='add_stats'),
    path('add/', Add_Stats.as_view(template_name="psmf/add_stats_view.html"), name='add_stats'),
    path('', Stats.as_view(template_name='psmf_index.html'), name='psmf_index'),
    # path('about_me/', about, name='about'),

]
