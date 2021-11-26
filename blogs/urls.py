from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [

	#path('', views.index),
	path('', views.blogsHome, name='blogs-home'),
	path('blogs/', views.blogsHome, name='blogs-home'),
	path('about/', views.about, name='blogs-about'),
	path('login/', views.login, name='login'),
	path('signup/', views.signup, name='signup'),



]