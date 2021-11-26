from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts
from django.contrib.auth.models import User


# Create your views here.


'''def index(request):
	template= 'index.html'
	context = {}
	return render(request, template, context)'''

def blogsHome(request):
	template= 'blogs/blogs.html'
	'''posts= [
					{
						'author':'Soumyajit',
						'title':'Blog Post',
						'date_posted':'12/07/2021',
						'content':'First Post',
					},
					{
						'author':'Raju',
						'title': 'Blog Post',
						'date_posted':'08/01/2021',
						'content':'First Post',
					},
				]'''
	posts=Posts.objects.all()
	'''user=User.objects.filter(id=2).first()
				#posts=Posts.objects.filter(author_id=1)
				
				posts= user.posts_set.all()'''
	
	context={'posts': posts, 'page_title':'Blogs'}
	return render(request, template, context)

def about(request):
	template='blogs/aboutus.html'
	
	context={'page_title': 'About Us'}
	return render(request, template, context)

def login(request):
	template='blogs/login.html'
	context={'page_title': "Login"}
	return render(request, template, context)

def signup(request):
	template='blogs/signup.html'
	context={'page_title': 'Sign Up'}
	return render(request, template, context)