from django.shortcuts import render

# Create your views here.

def groupme(request):
	return render(request, 'groupme/groupme.html', {})