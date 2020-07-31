from django.contrib import admin
from task.models import Task, TaskList

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ('description', 'created', 'is_complete')

class TaskInline(admin.TabularInline):
	model = Task

class TaskListAdmin(admin.ModelAdmin):
	list_display = ('title', 'created')
	inlines = [TaskInline]

admin.site.register(TaskList, TaskListAdmin)
admin.site.register(Task, TaskAdmin)
