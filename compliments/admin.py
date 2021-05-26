from django.contrib import admin
from .models import Compliments
# Register your models here.
@admin.register(Compliments)
class Compliments(admin.ModelAdmin):
    list_display = ('person', 'compliment', 'category')