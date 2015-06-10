from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from .models import EngineeringAmbassador

from itertools import chain

import time


@login_required(login_url='/login/')
def profile(request):
    stylesheet = 'personal/profile.css'
    app = 'personal'
    ambassador = get_object_or_404(EngineeringAmbassador, user = request.user)
    profile_pic = ambassador.picture.url
    
    events_registered = sorted(chain(request.user.outreach.all(), request.user.tours.all()), key=lambda instance: instance.date)
    
    if request.POST:
        
        fall_status = request.POST.getlist('fall_status')
        spring_status = request.POST.getlist('spring_status')
        
        ambassador.grad_date = request.POST['grad_date']
        
        if not fall_status:
            ambassador.fall_status = False
        else:
            ambassador.fall_status = True
            
        if not spring_status:
            ambassador.spring_status = False
        else:
            ambassador.spring_status = True
            
        ambassador.student_id = request.POST['student_id']
        ambassador.company_designation = request.POST['company_designation']
        ambassador.companies_worked = request.POST['companies_worked']
        
        ambassador.save()
            
            
    return render(request, 'personal/profile.html', {'stylesheet':stylesheet, 'app': app, 'profile_pic':profile_pic, 'ambassador':ambassador, 'events_registered':events_registered, })

@login_required(login_url='/login/')   
def edit(request):
    
    edit = True
    
    years = []
    
    for i in range(0,8):
        years.append(time.localtime()[0] + i)
    
    stylesheet = 'personal/profile.css'
    app = 'personal'
    ambassador = get_object_or_404(EngineeringAmbassador, user = request.user)
    profile_pic = ambassador.picture.url
    
    events_registered = sorted(chain(request.user.outreach.all(), request.user.tours.all()), key=lambda instance: instance.date)
    
    return render(request, 'personal/profile.html', {'stylesheet':stylesheet, 'app': app, 'profile_pic':profile_pic, 'ambassador':ambassador, 'events_registered':events_registered, 'edit':edit, 'years':years}) 
        
    

