from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

def index(request):
	return render(request, 'index.html', {})

def register(request):
	
	if request.POST:
	
		#create a template form to post this data
		username = request.POST['username']
		#first_name = request.POST['first_name']
		#last_name = request.POST['last_name']
		email = request.POST['email']
		password = request.POST['password']
		
		newuser = User.objects.create_user(username, email, password)
		
		#user.first_name, user.last_name = first_name, last_name
			
		newuser.save()
		
		user = authenticate(username=newuser.username,password=password)
		
		if user is not None:
			
			if user.is_active:
				login(request, user)
				return HttpResponse('success!')
			else:
				return HttpResponse('Not valid')
		else:
			return HttpResponse('Cannot Register')
		
	return render(request, 'register.html', {})
		
	
		
		
		
		
		
			
