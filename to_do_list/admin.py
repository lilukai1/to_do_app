from django.contrib import admin
from to_do_list.models import Task, TaskRelationship, Project

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", 'project', 'project_id', "person", "time_began", "time_ended", "priority", "completed")

admin.site.register(TaskRelationship)

class TaskRelationshipInline(admin.StackedInline):
    model = TaskRelationship
    fk_name = 'current_task'
    list_display = ("current_task", "target_task", "relationship", "project")

admin.site.register(Project)

class Project(admin.StackedInline):
    model=Project

