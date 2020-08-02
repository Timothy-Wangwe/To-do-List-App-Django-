from django.shortcuts import render, get_object_or_404, redirect

from task.forms import TaskListForm, TaskForm
from task.models import TaskList, Task

from django.utils import timezone

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
				created=timezone.now(),
				)
			tasklist.save()
			return redirect('task:task_list')

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
				created=timezone.now(),
				)
			task.save()
			return redirect('task:task_display', pk)

	task_list = get_object_or_404(TaskList, pk=pk)
	tasks = task_list.tasks.all()
	length = task_list.count()
	complete_length = task_list.count_complete()
	incomplete_length = task_list.count_incomplete()
	if length != 0:
		progress = round((complete_length/length)*100, 0)
	context = {
		'task_list':task_list,
		'tasks':tasks,
		'len':length,
		'complete':complete_length,
		'incomplete':incomplete_length,
		'progress':progress,
		'form':TaskForm(),
		}
	return render(request, 'task/tasks.html', context)

def delete_list(request, pk):
	tasklist = TaskList(id = pk)
	tasklist.delete()
	return redirect('task:task_list')

def complete_task(request, pk, list_id):
	task = Task(id = pk, tasklist_id=list_id)
	task.description = Task.objects.get(pk=pk).description
	task.is_complete = True
	task.completed_at = timezone.now()
	task.save()
	return redirect('task:task_display', list_id)

def restart_task(request, pk, list_id):
	task = Task(id = pk, tasklist_id=list_id)
	task.description = Task.objects.get(pk=pk).description
	task.is_complete = False
	task.completed_at = None
	task.save()
	return redirect('task:task_display', list_id)
