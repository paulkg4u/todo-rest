from django.conf.urls import url

from .views import *

urlpatterns = [
	url(r'^Todo/(?P<uuid>[A-Za-z0-9]{36})^$', TodoDetailView.as_view()),
	url(r'^Todo/', TodoView.as_view()),
	url(r'^Registration/', RegistrationView.as_view())
]