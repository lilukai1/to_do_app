from django.contrib import admin
from to_do_list.models import Task, TaskRelationship
# from .models import Account
# # Register your models here.
# @admin.register(Account)
# class AccountAdmin(admin.ModelAdmin):
#     list_display = ("username", "email", "first_name", "last_name")
# admin.site.register(Task)
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "person", "time_began", "time_ended", "priority", "completed")

# @admin.register(TaskRelationship)
admin.site.register(TaskRelationship)
class TaskRelationshipInline(admin.StackedInline):
    model = TaskRelationship
    fk_name = 'current_task'
    list_display = ("current_task", "target_task", "relationship")