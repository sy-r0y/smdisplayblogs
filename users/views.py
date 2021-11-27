

from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm  # Built-in Django user-creations form
from django.contrib import messages
from .userforms import UserSignupForm


# Create your views here.

def login(request):

	template='users/login.html'
	context={'page_title': "User Login"}
	return render(request, template, context)

def signup(request):

	if request.method == 'POST':  # check if the request is a post request(trigged when form is submitted)
		form= UserSignupForm(request.POST)  # grab the form data which was submitted as the POST request
		
		if form.is_valid():  # check if the fields are correct/valid. Django does this automagically
			
			form.save()  # save() submits & saves the user data to the database. Django does this automagically

			username= form.cleaned_data.get('username')  # UserCreationForm() creates a form with 'username' field
														 # validated form data will be captured- 
														 # from the form.cleaned_data dictionary
														 # this will have been converted into Python types for us from the form
														 # Django does this in the background

			# Use Flash Message to show we've received valid data
			# Diffrent types of messages are availabe(messages.debug, messages.info, messages.success, messages.warning, messages.error)
			
			messages.success(request, f'Created account for {username}')

			#messages.warning(request, "warning baby") # we can flash any number of messages

			# redirect user to home page once form is successfully submitted
			return redirect('blogs-home')

	else:
		form = UserSignupForm()  # instantiate an empty form with any pre-entered data 

	template='users/signup.html'

	context={'page_title': 'User Signup', 'form': form}
	
	return render(request, template, context)
