from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
import json
from django.contrib.auth.models import User
from personal.models import EngineeringAmbassador
from fuzzywuzzy import fuzz
from django.db.models import Q

# Create your views here.
def directory(request):
    stylesheet = "directory/directory.css"
    script = "directory/directory.js"
    
    users = User.objects.all().order_by("first_name")
    ambassadors = []
    
    for user in users:
        ambassador = get_object_or_404(EngineeringAmbassador, user = user)
        ambassadors.append(ambassador)
    
    return render(request,'directory/directory.html',{'stylesheet':stylesheet, 'script':script, 'ambassadors':ambassadors})
 
#http://flaviusim.com/blog/AJAX-Autocomplete-Search-with-Django-and-jQuery/   for some help
def names(request):
    if request.is_ajax():
        
        # parse the GET request for the query "term" and lowercase it
        query = request.GET.get('term', '')
        query = query.lower()
                
        #get a django query object containing all ambassadors
        ambassadors = User.objects.all()
        
        #make a dict to store ambassador and full name as key value pair   
        ambassador_names = {}
        matching = []
        
        # populate ambassador_names
        for ambassador in ambassadors:
            key = ambassador
            value = ambassador.first_name + " " + ambassador.last_name
            ambassador_names[key] = value
        
        #this is the beast code that 
            #1) goes through ambassador_names and checks if the term query is in the ambassador name or fuzzy matches it
            #2) if so get each ambassadors profile and make a dictionary for the final json of the ambassador's name, major, picture_url ...
            #3) append it to the json list
            #4) dump the list into a json object
            
        for ambassador in ambassador_names.iterkeys():#.iterkeys() is specifically used otherwise Django won't let me iterate through users as keys
            name = ambassador_names[ambassador]
            match_ratio = fuzz.partial_ratio(query, name)
            if match_ratio > 75 or query in name.lower():
                profile = get_object_or_404(EngineeringAmbassador, user=ambassador)
                ambassador_json = {}
                ambassador_json['full_name'] = name
                ambassador_json['major'] = profile.major
                ambassador_json['picture'] = profile.picture.url
                matching.append(ambassador_json)
            data = json.dumps(matching)
    else:
        data = 'This needs to be an AJAX request'
     
    response = JsonResponse(data, safe=False)
    return response
    