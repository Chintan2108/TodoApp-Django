from django.db import models
from todo.forms import TASK_PRIORITIES

class Todo(models.Model):
    text = models.CharField(max_length=40, unique=True)
    complete = models.BooleanField(default=False)
    priority = models.IntegerField(choices=TASK_PRIORITIES, default=2)
    

    def __str__(self):
        return self.text