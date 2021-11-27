# URLs 


from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns=[

	#path('', views.index),
	path('login/', views.login, name='users-login'),
	path('signup/', views.signup, name='users-signup'),


]