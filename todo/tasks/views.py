from django.shortcuts import render
from django.http import HttpResponse
from .models import Tasks

def summary_view(request): 
    tasks = Tasks.objects.all()
    return render(request, 'index.html', {'tasks': tasks})
    
def new_view(request):
    return HttpResponse("New tasks come here...")


def done_view(request):
    return HttpResponse("Finished tasks come here...")

