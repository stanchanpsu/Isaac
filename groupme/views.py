from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json

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
			script = 'groupme/chat.js'
			return render(request, 'groupme/groupme.html',{'access_token':request.session['access_token'], 'stylesheet':stylesheet, 'script':script,})
			
		#if user is logged out of groupme
		else:
			auth_url = 'https://oauth.groupme.com/oauth/authorize?client_id=bnveOko8sTysD27ugGxOL5HhPeBmrxhzmXdewuXarxi50FOk'
			return render(request, 'groupme/groupme.html',{'auth_url':auth_url,})

@login_required(login_url='/login/')
def token(request):			
	if request.is_ajax():
		if 'access_token' in request.session:
			token = {'token':request.session['access_token']}
			token = json.dumps(token)
			response = JsonResponse(token,safe=False)
			return response
		else:
			return redirect('/groupme/')
	else:
		return redirect('/groupme/')
		