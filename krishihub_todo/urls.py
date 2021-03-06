"""krishihub_todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import  url
from rest_framework import routers
from rest_framework.documentation import include_docs_urls

router = routers.DefaultRouter()

urlpatterns = [
	path('',include(router.urls)),
	path('todo/', include('todo.urls')),
	path('docs/',include_docs_urls(title = "Todo - Rest", authentication_classes=[], permission_classes=[], public=True)),
    path('admin/', admin.site.urls),
	url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]
