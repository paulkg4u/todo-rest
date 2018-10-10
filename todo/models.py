from django.db import models
from django.utils import timezone
from uuid import uuid4

from django.contrib.auth.models import User, UserManager


# Create your models here.


class TodoUser(User):
	uuid = models.UUIDField(primary_key=True, default=uuid4)
	objects = UserManager()

	def __str__(self):
		return  str(self.first_name + ' '+self.last_name)

class Todo(models.Model):
	uuid = models.UUIDField(primary_key=True, editable=False, default=uuid4)
	title = models.CharField(max_length = 100)
	description = models.TextField(default = "")
	createdAt = models.DateTimeField(default = timezone.now)
	dueDate = models.DateTimeField(null = True, blank = True)
	user = models.ForeignKey(TodoUser, null = True, blank=True, on_delete= models.CASCADE)
	isComplete = models.BooleanField(default=False)


	def __str__(self):
		return  str(self.title)


