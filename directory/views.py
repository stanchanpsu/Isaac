from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
import json, operator
from django.contrib.auth.models import User
from personal.models import EngineeringAmbassador
from fuzzywuzzy import fuzz
from django.db.models import Q
from itertools import chain

@login_required(login_url='/login/')
def directory(request):
    
    app = 'directory'
    
    if request.GET and 'directory_search' in request.GET:
        
        stylesheet = 'personal/profile.css'
        
        directory_search = request.GET['directory_search']
        if directory_search is not None and directory_search != '':
            ambassadors = User.objects.all()
            matching = []
            for term in directory_search.split():
                matching_ambassadors = ambassadors.filter( Q(first_name__contains = term) | Q(last_name__contains = term)).order_by('first_name')
                for matching_ambassador in matching_ambassadors:
                    matching.append(matching_ambassador)
            if not matching:
                return redirect('/directory/')
            else:
                match = get_object_or_404(User, username = matching[0])
                ambassador = get_object_or_404(EngineeringAmbassador, user = match)
                events_registered = match.event.all()
                return render(request, 'directory/ambassador_profile.html', {'stylesheet':stylesheet, 'app': app, 'ambassador':ambassador, 'events_registered':events_registered, })
        else:
            return redirect('/directory/')
            
    else:
        stylesheet = "directory/directory.css"
        script = "directory/directory.js"
        
        users = User.objects.all().order_by("first_name")
        ambassadors = []
        
        for user in users:
            ambassador = get_object_or_404(EngineeringAmbassador, user = user)
            ambassadors.append(ambassador)
        
        return render(request,'directory/directory.html',{'stylesheet':stylesheet, 'app':app,'script':script, 'ambassadors':ambassadors})
 
#http://flaviusim.com/blog/AJAX-Autocomplete-Search-with-Django-and-jQuery/   for some help
@login_required(login_url='/login/')
def names(request):
    if request.is_ajax():
        
        # parse the GET request for the query "term" and lowercase it
        query = request.GET.get('term', '')
        query = query.lower()
                
        #get a django query object containing all ambassadors
        ambassadors = User.objects.all().order_by('first_name')
        
        #make a dict to store ambassador and full name as key value pair   
        ambassador_names = {}
        # ambassador_names_sorted = sorted(ambassador_names.items(), key=operator.itemgetter(1))
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
                ambassador_json['id'] = profile.user.id
                ambassador_json['full_name'] = name
                ambassador_json['major'] = profile.major
                ambassador_json['picture'] = profile.picture.url
                ambassador_json['aboutme'] = profile.aboutme
                matching.append(ambassador_json)
            data = json.dumps(matching)
    else:
        data = 'This needs to be an AJAX request'
     
    response = JsonResponse(data, safe=False)
    return response

@login_required(login_url='/login/')    
def ambassador_profile(request, ambassador_id = None):
    
    if request.GET and 'directory_search' in request.GET:
        
        stylesheet = 'personal/profile.css'
        app = 'directory'
        
        directory_search = request.GET['directory_search']
        if directory_search is not None and directory_search != '':
            ambassadors = User.objects.all()
            matching = []
            for term in directory_search.split():
                matching_ambassadors = ambassadors.filter( Q(first_name__contains = term) | Q(last_name__contains = term))
                for matching_ambassador in matching_ambassadors:
                    matching.append(matching_ambassador)
            if not matching:
                return redirect('/directory/')
            else:
                match = get_object_or_404(User, username = matching[0])
                ambassador = get_object_or_404(EngineeringAmbassador, user = match)
                events_registered = match.event.all()
                return render(request, 'directory/ambassador_profile.html', {'stylesheet':stylesheet, 'app': app, 'ambassador':ambassador, 'events_registered':events_registered, })
        else:
            return redirect('/directory/')
    
    stylesheet = 'personal/profile.css'
    app = 'directory'
    user = get_object_or_404(User, id = ambassador_id)
    ambassador = get_object_or_404(EngineeringAmbassador, user = user)
    events_registered = user.event.all()
    
    return render(request, 'directory/ambassador_profile.html', {'stylesheet':stylesheet, 'app': app, 'ambassador':ambassador, 'events_registered':events_registered, })
    
    