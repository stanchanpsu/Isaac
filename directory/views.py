from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from personal.models import EngineeringAmbassador
from django.db.models import Q

# Create your views here.
def directory(request):
    return render(request,'directory/directory.html',{})
 
# http://flaviusim.com/blog/AJAX-Autocomplete-Search-with-Django-and-jQuery/   
def names(request):
    if request.is_ajax():
        query = request.GET.get('term', '')
        
        ambassadors = EngineeringAmbassador.objects.filter(object__contains = query)   
        names = []
        
        # for user in User.objects.filter(Q(first_name__contains = query) | Q(last_name__contains = query))[:20]:
        #     names.append(user.first_name + " " + user.last_name)
        
        for ambassador in ambassadors:
            names.append(ambassador)
            
        response = JsonResponse(names, safe=False)
        return response
    