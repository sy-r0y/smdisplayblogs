

from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def login(request):
	template='users/login.html'
	context={'page_title': "User Login"}
	return render(request, template, context)

def signup(request):
	form= UserCreationForm()

	template='users/signup.html'

	context={'page_title': 'User Signup', 'form': form}
	
	return render(request, template, context)
