from django.shortcuts import render, HttpResponse

def index(request):
	"""Displays the Landing page"""
	return HttpResponse("This thing is working")
