from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


from .models import Event,OutreachTrip,Tour
from .forms import EventView

#date formatting
from django.utils import formats

import time, json

app = 'events'
current_year = time.localtime()[0]

@login_required(login_url='/login/')
def list_events(request):
		
	title = 'EA events'
	stylesheet = 'events/list_events.css'
	
	# get selection from event_view dropdown
	event_view = request.GET.get('event_view', False)			
	
	outreach_list = OutreachTrip.objects.order_by('date')
	tour_list = Tour.objects.order_by('date')
	
	return render(request,'events/list_events.html', {'outreach_list':outreach_list, 'tour_list':tour_list, 'event_view': event_view, 'title':title, 'app': app, 'stylesheet':stylesheet, })	
	

@login_required(login_url='/login/')
def event_detail(request, event_type, event_id):
	
	request.session['event_type'], request.session['event_id'] = event_type, event_id
	
	# 1. parse the url (from regex capture) for type of event and event id (this is specific to type of event ie. both Tour and Outreach can have id = 1)	
	if event_type == 'outreach':
		event = get_object_or_404(OutreachTrip, pk = event_id)
		title = event.school + ' Outreach Trip'
		
	elif event_type == 'tour':
		event = get_object_or_404(Tour, pk = event_id)
		time = formats.date_format(event.time, "SHORT_TIME")
		title = event.get_tour_type_display() + ' Tour at ' + time
	
	# 2. set 'event_register' button value depending on whether EA is already registered
		
	if request.user in event.EAs_registered.all():
		event_register_status = "You are registered for this event."
		request.session['event_registered'] = True
		background_color = 'teal'
	else:
		event_register_status = "You are not registered for this event."
		request.session['event_registered'] = False
		background_color = 'red'
	
	# 3. if the user clicks the button, perform the correct action ( sign up or withdraw) and redirect to the same page - prevents incorrect resubmit of form
	
	if request.is_ajax():
		if event_toggle == 'Withdraw':
			event.EAs_registered.remove(request.user)
			event.save()
		elif event_toggle == 'Sign up':
			event.EAs_registered.add(request.user)
			event.save()
			
		return redirect("/events/" + event_type + "/" + event_id  +"/")
		
	# initial GET request or reload of page renders the page with correct context
				
	EAs_registered 	= event.EAs_registered.order_by('username')
	stylesheet = 'events/event_detail.css'
	script = 'events/event_detail.js'
		
	return render(request, 'events/event_detail.html', {'title':title, 'event':event, 'event_type':event_type, 'event_id':event_id, 'registered': request.session['event_registered'], 'EAs_registered':EAs_registered,'event_register_status':event_register_status, 'background_color':background_color,'stylesheet':stylesheet, 'script':script, 'app': app,})

@login_required(login_url='/login/')
def register(request):
	if request.is_ajax():
		events = Event.objects.order_by("pk")
		event = get_object_or_404(Event, pk=9)
		registered = request.session['event_registered']
		if registered:
			event.EAs_registered.remove(request.user)
			event.save()
		elif not registered:
			event.EAs_registered.add(request.user)
			event.save()
		return JsonResponse(json.dumps(str(events)), safe=False)