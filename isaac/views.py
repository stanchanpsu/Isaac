from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def index(request):
	# stylesheet = 'auth/style.css'
	
	if request.user.is_authenticated():
		return redirect("/events")
	
	else:
		title = 'Isaac Login'
		return render(request, 'login.html', {'title':title,})
	
def logout_user(request):
	logout(request)
	return redirect("/")
	
def login_user(request):
	
	if request.POST:
		username = request.POST['username']
		password = request.POST['password']
		
		user = authenticate(username=username,password=password)
		
		if user is not None:
			
			if user.is_active:
				login(request, user)
				return redirect("/")
			else:
				state = "you are not an active user, contact administrator"
				return render(request, "login.html", {'state':state})
		else:
			state = "login invalid, try again"
			return render(request,"login.html", {'state':state})
					
	return redirect("/")

#edit the template to include name fields
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
		
	
		
		
		
		
		
			
