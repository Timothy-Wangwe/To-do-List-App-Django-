from django.contrib import admin
from .models import Tasks

class TasksAdmin(admin.ModelAdmin):
    list_display = ('date', 'subject', 'description')

admin.site.register(Tasks, TasksAdmin)