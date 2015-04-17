from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def index(request):
	if request.user.is_authenticated():
		login_register = "logged in"
	else:
		login_register = "register"
	return render(request, 'index.html', {"login_register":login_register})
	
def logout_user(request):
	logout(request)
	return redirect("/auth")
	

def register(request):
	
	if request.POST:
	
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
		
	
		
		
		
		
		
			
