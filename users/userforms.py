

# userforms.py module would containe the neccessary logic for the user creation form

# it will inherit from the UserCreationForm()

from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User 

class UserSignupForm(UserCreationForm):
	
	email= forms.EmailField()

	class Meta:  # Meta class gives us a nested namespace for configurations & keeps all the configurations 
				 # in one place.
				 # Within the configuration we're saying that the "User" model would be affected 
				 # when we save the form(via form.save)

		model= User 
		fields= ['username', 'email', 'password1', 'password2'] # describe which fields we want in the form



