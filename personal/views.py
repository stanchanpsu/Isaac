from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from .models import EngineeringAmbassador

# from itertools import chain

import time


@login_required(login_url='/login/')
def profile(request):
    stylesheet = 'personal/profile.css'
    app = 'personal'
    ambassador = get_object_or_404(EngineeringAmbassador, user = request.user)
    try:
        profile_pic = ambassador.picture.url
    except:
        profile_pic = ""
        
    events_registered = request.user.event.all()
    
    if request.POST:
        
        fall_status = request.POST.getlist('fall_status')
        spring_status = request.POST.getlist('spring_status')
        schreyer_honors = request.POST.getlist('schreyer_honors')
        
        ambassador.grad_semester = request.POST['grad_semester']
        ambassador.grad_year = request.POST['grad_year']
        
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
        
        ambassador.major = request.POST['major']
        ambassador.major_2 = request.POST['major_2']
        ambassador.minor = request.POST['minor']
        ambassador.minor_2 = request.POST['minor_2']
        
        if not schreyer_honors:
            ambassador.schreyer_honors = False
        else:
            ambassador.schreyer_honors = True
        
        ambassador.phone = request.POST['phone']
        
        ambassador.aboutme = request.POST['aboutme']
        
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
    grad_year = int(ambassador.grad_year)
    
    events_registered = request.user.event.all()
    
    return render(request, 'personal/profile.html', {'stylesheet':stylesheet, 'app': app, 'profile_pic':profile_pic, 'ambassador':ambassador, 'events_registered':events_registered, 'edit':edit, 'years':years,'grad_year':grad_year,}) 
        
    

