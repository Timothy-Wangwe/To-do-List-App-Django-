from django.shortcuts import render
from django.http import HttpResponse


def summary_view(request):
    return HttpResponse("A summary of all tasks come here...")
    
def new_view(request):
    return HttpResponse("New tasks come here...")


def done_view(request):
    return HttpResponse("Finished tasks come here...")