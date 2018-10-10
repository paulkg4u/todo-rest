from rest_framework import serializers
from .models import TodoUser, Todo

class TodoUserSerializer(serializers.ModelSerializer):

	def create(self, validated_data):
		userObject = TodoUser.objects.create_user(**validated_data)
		return {'todoUser':userObject}

	class Meta:
		model = TodoUser
		fields = ('username', 'email', 'first_name', 'last_name', 'password')


class TodoSerializer(serializers.ModelSerializer):


	def create(self, validated_data):
		todoObject = Todo.objects.create(**validated_data)
		return todoObject

	def update(self,instance,validated_data):
		todoObject = Todo.objects.filter(uuid = instance.uuid).update(**validated_data)
		return  instance

	class Meta:
		model = Todo
		fields = ('title','description','uuid','createdAt','dueDate','user','isComplete')


