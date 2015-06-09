from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from .models import EngineeringAmbassador

from itertools import chain


@login_required(login_url='/login/')
def profile(request, edit_status = None):
    stylesheet = 'personal/profile.css'
    app = 'personal'
    ambassador = get_object_or_404(EngineeringAmbassador, user = request.user)
    profile_pic = ambassador.picture.url
    
    edit = False
    
    events_registered = sorted(chain(request.user.outreach.all(), request.user.tours.all()), key=lambda instance: instance.date)
    
    if request.POST:
        if edit_status == 'edit':
            edit = True
            return render(request, 'personal/profile.html', {'stylesheet':stylesheet, 'app': app, 'profile_pic':profile_pic, 'ambassador':ambassador, 'events_registered':events_registered, 'edit':edit,})
            
        else:
            edit = False
            
            
    return render(request, 'personal/profile.html', {'stylesheet':stylesheet, 'app': app, 'profile_pic':profile_pic, 'ambassador':ambassador, 'events_registered':events_registered, 'edit':edit,})
        
    

