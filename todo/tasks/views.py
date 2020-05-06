from django.shortcuts import render
from django.http import HttpResponse
from .models import Tasks
from .forms import TasksForm

def summary_view(request): 
    tasks = Tasks.objects.all()
    return render(request, 'index.html', {'tasks': tasks})
    
def new_view(request):
    return HttpResponse("New tasks come here...")


def done_view(request):
    return HttpResponse("Finished tasks come here...")

def task_form(request):
    form = TasksForm()
    return render(request, 'new_task.html')