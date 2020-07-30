from django.contrib import admin
from task.models import Task, TaskList

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ('description', 'created', 'is_complete')

class TaskListAdmin(admin.ModelAdmin):
	list_display = ('title', 'created')

admin.site.register(TaskList, TaskListAdmin)
admin.site.register(Task, TaskAdmin)
