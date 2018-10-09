from django.shortcuts import render
from rest_framework import  status
from rest_framework.views import APIView
from rest_framework.response import  Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated


from .models import Todo, User
from .serializers import UserSerializer
# Create your views here.




class RegistrationView(APIView):
	def post(self, request):
		data = request.data
		serializer = UserSerializer(data = data)
		if serializer.is_valid():
			userObject = serializer.save()
			print(userObject)
			return  Response({'success': True},status = status.HTTP_200_OK)
		else:
			print(serializer.errors)
			return  Response({'success' : False}, status = status.HTTP_200_OK)





class TodoDetailView(APIView):

	permission_classes = [IsAuthenticated]
	def get(self, request, uuid):
		"""
		Get details about a todo
		:param request:
		:param uuid:
		:return:
		"""
		print(uuid)
		return  Response({}, status = status.HTTP_200_OK)


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
		user_uuid = request.query_params.get('uuid')
		User.objects.get(uuid = user_uuid)
		todos = Todo.objects.filter(user = User)
		return  Response({}, status = status.HTTP_200_OK)

	def post(self, request):
		"""
		Create new Todo
		:param request:
		:return:
		"""
		data = request.data
		print(data)
		return Response({}, status = status.HTTP_200_OK)

