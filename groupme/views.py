from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def groupme(request):
    
    if request.GET and 'access_token' in request.GET:
        access_token = request.GET['access_token']
    
	return render(request, 'groupme/groupme.html', {})