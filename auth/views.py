from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse

def register(request):
	
	if request.POST:
	
		#create a template form to post this data
		username = request.POST['username']
		#first_name = request.POST['first_name']
		#last_name = request.POST['last_name']
		email = request.POST['email']
		password = request.POST['password']
		
		user = User.objects.create_user(username, email, password)
		
		#user.first_name, user.last_name = first_name, last_name
			
		user.save()
		
		return HttpResponse('success!')
		
	return render(request, 'register.html', {})
		
		
		
		
		
		
		
			
