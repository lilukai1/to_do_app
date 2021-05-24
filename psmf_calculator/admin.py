from django.contrib import admin
from psmf_calculator.models import Stats


@admin.register(Stats)
class PSMF(admin.ModelAdmin):
    list_display = ('person', 'weight', 'height', 'age', 'activity', 'gender', 'timestamp')