from django.db import models
from django.utils import timezone

class TaskList(models.Model):
	title = models.CharField(max_length=20)
	created = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ('created',)

	def __str__(self):
		return self.title

	def count(self):
		return self.tasks.count()

	def count_complete(self):
		return self.tasks.filter(is_complete=True).count()

	def count_incomplete(self):
		return self.tasks.filter(is_complete=False).count()


class Task(models.Model):
	tasklist = models.ForeignKey(TaskList, related_name='tasks', on_delete=models.CASCADE)
	description = models.CharField(max_length=255)
	created = models.DateTimeField(auto_now=True)
	completed_at = models.DateTimeField(null=True)
	is_complete = models.BooleanField(default=False)

	class Meta:
		ordering = ('tasklist', 'created', 'completed_at')

	def __str__(self):
		return self.description

	def complete(self):
		self.is_complete = True
		self.completed_at = timezone.now()
		self.save()

	def restart(self):
		self.is_complete = False
		self.completed_at = None
		self.save()