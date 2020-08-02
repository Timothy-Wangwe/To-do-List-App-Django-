from django.urls import path
from .views import index, task_list, task_display, delete_list, complete_task, restart_task

app_name = 'task'
urlpatterns = [
	path('', index, name='index'),
	path('lists/', task_list, name='task_list'),
	path('lists/<int:pk>/', task_display, name='task_display'),
	path('lists/<int:pk>/delete/', delete_list, name='delete_list'),
	path('lists/<int:list_id>/task/<int:pk>/done/', complete_task, name='complete_task'),
	path('lists/<int:list_id>/task/<int:pk>/undo/', restart_task, name='restart_task'),
]