from django.db import models
from django.utils import timezone
from uuid import uuid4

from django.contrib.auth.models import AbstractBaseUser, User
# Create your models here.


class Todo(models.Model):
	uuid = models.UUIDField(primary_key=True, editable=False, default=uuid4())
	title = models.CharField(max_length = 100)
	description = models.TextField(default = "")
	createdAt = models.DateTimeField(default = timezone.now())
	dueDate = models.DateTimeField(null = True, blank = True)

	def __str__(self):
		return  str(self.name)


class User(AbstractBaseUser):
	uuid = models.UUIDField(primary_key=True, editable=False,default=uuid4())
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	email = models.CharField(unique=True,max_length=200)
	username = models.CharField(unique=True,max_length=200)
	def __str__(self):
		return str(self.first_name+' '+self.last_name)



    

