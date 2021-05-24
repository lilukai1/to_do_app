from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from psmf_calculator.models import Stats
from django.contrib.auth.decorators import login_required

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class Stats(ListView):
    model = Stats
    context_object_name = 'stats'
    print(Stats.objects.all())
    # def get_context_data(self, **kwargs):
    #     print(**kwargs)
    #     context = super().get_context_data(**kwargs)
    #     context["page_title"] = f"{kwargs['person'].title} Detail"
    #     return context  


class Add_Stats(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Stats
    context_object_name = 'stats'
    fields = [ 'weight', 'height', 'gender', 'activity', 'birthday']
    # def get_context_data(self, **kwargs):
    #     print(**kwargs)
    #     context = super().get_context_data(**kwargs)
    #     context["page_title"] = f"{kwargs['person'].title} Detail"
    #     return context

    def get_success_message(self, cleaned_data):
        return "Stats Added!"