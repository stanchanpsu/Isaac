from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from .models import EngineeringAmbassador


@login_required(login_url='/login/')
def profile(request):
    stylesheet = 'personal/profile.css'
    ambassador = get_object_or_404(EngineeringAmbassador, user = request.user)
    profile_pic = ambassador.picture.url
    return render(request, 'personal/profile.html', {'stylesheet':stylesheet,'profile_pic':profile_pic, 'ambassador':ambassador})
