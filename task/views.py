from django.shortcuts import render, HttpResponse

def index(request):
	"""Displays the Landing page"""
	return render(request, 'task/index.html', {})
