from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User

# Create your views here.
def directory(request):
    return render(request,'directory/directory.html',{})
 
# http://flaviusim.com/blog/AJAX-Autocomplete-Search-with-Django-and-jQuery/   
def names(request):
    names = []
    for user in User.objects.all():
        names.append(user.first_name + " " + user.last_name)
        
    response = JsonResponse(names, safe=False)
    return response
    