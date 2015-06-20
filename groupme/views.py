from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def groupme(request):
    
	# if groupme callbacks with the access token of the user
	if request.GET and 'access_token' in request.GET:
		request.session['access_token'] = request.GET['access_token']
		access_token = request.session['access_token']
		
		return redirect('/groupme/')
	
	# if regular page request by user	
	else:
		# if user logged into groupme
		if 'access_token' in request.session:
			stylesheet = 'groupme/chat.css'
			return render(request, 'groupme/groupme.html',{'access_token':request.session['access_token'], 'stylesheet':stylesheet,})
			
		#if user is logged out of groupme
		else:
			auth_url = 'https://oauth.groupme.com/oauth/authorize?client_id=bnveOko8sTysD27ugGxOL5HhPeBmrxhzmXdewuXarxi50FOk'
			return render(request, 'groupme/groupme.html',{'auth_url':auth_url,})