from django.shortcuts import render
from django.http import HttpResponse


def summary_view(request):
    # tasks = Tasks.objects.all()
    return render(request, 'index.html')
    
def new_view(request):
    return HttpResponse("New tasks come here...")


def done_view(request):
    return HttpResponse("Finished tasks come here...")