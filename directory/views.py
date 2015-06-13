from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.models import User
from personal.models import EngineeringAmbassador
from fuzzywuzzy import fuzz
from django.db.models import Q

# Create your views here.
def directory(request):
    stylesheet= "directory/directory.css"
    
    users = User.objects.all().order_by("first_name")
    ambassadors = []
    
    for user in users:
        ambassador = get_object_or_404(EngineeringAmbassador, user = user)
        ambassadors.append(ambassador)
    
    return render(request,'directory/directory.html',{'stylesheet':stylesheet, 'ambassadors':ambassadors})
 
# http://flaviusim.com/blog/AJAX-Autocomplete-Search-with-Django-and-jQuery/   
def names(request):
    if request.is_ajax():
        query = request.GET.get('term', '')
        query = query.lower()
        ambassadors = User.objects.all()
           
        ambassador_names = []
        matching = []
        
        for ambassador in ambassadors:
            name = ambassador.first_name + " " + ambassador.last_name
            ambassador_names.append(name)
        
        for ambassador_name in ambassador_names:
            match_ratio = fuzz.partial_ratio(query, ambassador_name)
            if match_ratio > 50 or query in ambassador_name.lower():
                matching.append(ambassador_name)
            
        response = JsonResponse(matching, safe=False)
        return response
    