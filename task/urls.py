from django.urls import path
from .views import index, task_list, task_display

app_name = 'task'
urlpatterns = [
	path('', index, name='index'),
	path('lists/', task_list, name='task_list'),
	path('lists/<int:pk>/', task_display, name='task_display'),
]