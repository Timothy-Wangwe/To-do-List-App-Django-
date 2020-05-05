from django.db import models

class Tasks(models.Model):
    date = models.DateTimeField(auto_now=False, null = False)
    subject = models.CharField(max_length = 200)
    description = models.CharField(max_length = 2000)