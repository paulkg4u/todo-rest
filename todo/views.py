from django.shortcuts import render
from rest_framework import  status
from rest_framework.views import APIView
from rest_framework.response import  Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated


from .models import Todo, TodoUser
from .serializers import TodoUserSerializer, TodoSerializer

from datetime import timedelta
from django.utils import timezone
# Create your views here.




class RegistrationView(APIView):

	def post(self, request):
		"""

		:param username: username
		:param email : email
		|
		:param first_name : First name of the user
		:param last_name : Last Name of the user
		:param password : password to be used

		:return: Success True if user created successfully, else error message
		"""
		data = request.data
		serializer = TodoUserSerializer(data = data)
		if serializer.is_valid():
			userObject = serializer.save()
			return  Response({'success': True},status = status.HTTP_200_OK)
		else:
			return  Response({'success' : False, 'errors': serializer.errors}, status = status.HTTP_200_OK)





class TodoDetailView(APIView):

	permission_classes = [IsAuthenticated]
	def get(self, request, uuid):
		"""
		Get details about a todo
		:param uuid: UUID of the todo object
		:return: Serialized todo object
		"""

		todo = Todo.objects.get(uuid = uuid)
		serializer =TodoSerializer(todo).data
		return  Response(serializer, status = status.HTTP_200_OK)


class TodoView(APIView):
	"""
	View to handle all todos related to a user
	"""
	permission_classes = [IsAuthenticated]
	def get(self, request):

		"""
		Get all todos associated with a user
		:param request:
		:param uuid: UUID of the user
		:return:Serialized list of all todos asociated with the user
		"""
		username = request.user

		user = TodoUser.objects.get(username = username)
		now = timezone.now()

		upcoming = Todo.objects.filter(dueDate__gte=now, isComplete=False,user = user)
		pending = Todo.objects.filter(dueDate__lte=now, isComplete=False, user = user)
		completed = Todo.objects.filter(user = user, isComplete=True)
		completedTodos= TodoSerializer(completed, many = True).data
		upcomingTodos = TodoSerializer(upcoming, many=True).data
		pendingTodos = TodoSerializer(pending, many=True).data
		return  Response({'completed':completedTodos,'upcoming':upcomingTodos,'pending':pendingTodos}, status = status.HTTP_200_OK)

	def post(self, request):
		"""
		Create new Todo
		:param request:
		:return:
		"""
		username = request.user
		data = request.data
		# user = TodoUser.objects.get(username = username)
		# data['user']= user.uuid
		serializer = TodoSerializer(data = data)
		if serializer.is_valid():
			todo = serializer.save()
			return Response(serializer.data, status=status.HTTP_200_OK)
		else:
			return Response(serializer.errors, status=status.HTTP_200_OK)

	def put(self, request):
		"""

		:param request:
		:return:
		"""
		data = request.data
		todo = Todo.objects.get(uuid = data['uuid'])

		serializer = TodoSerializer(todo,data = data, partial=True)
		if serializer.is_valid():
			todo = serializer.save()
			return Response(serializer.data, status=status.HTTP_200_OK)
		else:
			return Response(serializer.errors, status= status.HTTP_200_OK)




