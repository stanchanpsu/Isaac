from django.shortcuts import render
from django.contrib.auth import authenticate, login

# Create your views here.
def login_user(request):
	state = "Please log in below..."
	username = password = ''
	if request.POST:
		username = request.POST['username']
		password = request.POST['password']
		
		user = authenticate(username, password)
		if user is not None:
			if user.is_active:
				login(request, user)
				state = "You logged in, successfully."
			else:
				 state = "account is inactive"
		else: 
			state = 'username or password incorrect'
	return render(request, 'login.html', {'state':state, 'username': username})
