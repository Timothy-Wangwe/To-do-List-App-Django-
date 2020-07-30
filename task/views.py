from django.shortcuts import render, get_object_or_404

from task.forms import TaskListForm, TaskForm
from task.models import TaskList, Task

from datetime import datetime

def index(request):
	"""Displays the Landing page"""
	context = {'form':TaskListForm()}
	return render(request, 'task/index.html', context)

def task_list(request):
	"""Handles form from the landing(index) page and sends a list of task lists for display on 'lists' page"""
	if request.method == 'POST':
		form = TaskListForm(request.POST)
		if form.is_valid():
			tasklist = TaskList(
				title=request.POST['title'],
				created=datetime.now(),
				)
			tasklist.save()

	tasklists = TaskList.objects.all().reverse() #Latest comes first
	length = len(tasklists)
	context = {
		'form':TaskListForm(),
		'len':length,
		'tasklists':tasklists
		}
	return render(request, 'task/lists.html', context)

def task_display(request, pk):
	if request.method == 'POST':
		form = TaskForm(request.POST)
		if form.is_valid():
			task = Task(
				tasklist_id = pk,
				description=request.POST['description'],
				created=datetime.now(),
				)
			task.save()

	task_list = get_object_or_404(TaskList, pk=pk)
	tasks = task_list.tasks.all()
	length = len(tasks)
	context = {
		'task_list':task_list,
		'tasks':tasks,
		'len':length,
		'form':TaskForm(),
		}
	return render(request, 'task/task.html', context)
