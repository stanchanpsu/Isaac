from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


from .models import Event,OutreachTrip,Tour, MyCoe, FreshmanSeminar, ENGRClass
from .forms import EventView

#date formatting
from django.utils import formats

import datetime, time, json

app = 'events'
current_year = time.localtime()[0]
current_month = time.localtime()[1]
current_day = time.localtime()[2]
current_hour = time.localtime()[3]
current_minute = time.localtime()[4]

@login_required(login_url='/login/')
def list_events(request):
		
	title = 'EA events'
	stylesheet = 'events/list_events.css'
	
	# get selection from event_view dropdown
	event_view = request.GET.get('event_view', False)
	
	outreach_list = OutreachTrip.objects.order_by('date') #filter only dates past today's date
	tour_list = Tour.objects.filter(date__gte=datetime.date(current_year,current_month,current_day)).order_by('date')
	mycoe_list = MyCoe.objects.filter(date__gte=datetime.date(current_year,current_month,current_day)).order_by('date')
	freshman_list = FreshmanSeminar.objects.filter(date__gte=datetime.date(current_year,current_month,current_day)).order_by('date')
	class_list = ENGRClass.objects.filter(date__gte=datetime.date(current_year,current_month,current_day)).order_by('date')
	
	return render(request,'events/list_events.html', {'outreach_list':outreach_list, 'tour_list':tour_list, 'mycoe_list': mycoe_list, 'freshman_list':freshman_list, 'class_list': class_list, 'event_view': event_view, 'title':title, 'app': app, 'stylesheet':stylesheet, })	
	

@login_required(login_url='/login/')
def detail(request, event_id):
	
	# 1. parse the url (from regex capture) for event id
	
	event = get_object_or_404(Event, pk = event_id)
	request.session['event_id'] = event_id
	title = event

	# 2. set 'event_register' button value depending on whether EA is already registered
		
	if request.user in event.EAs_registered.all():
		event_register_status = "You are registered for this event."
		request.session['event_registered'] = True
		background_color = 'teal'
	else:
		event_register_status = "You are not registered for this event."
		request.session['event_registered'] = False
		background_color = 'red'
		
	# 3. figure out if event needs more EAs
	
	if event.EAs_needed <= 0:
		need = False
		if not request.session['event_registered']:
			background_color = "grey disabled white-text"
	else:
		need = True
		
	# initial GET request or reload of page renders the page with correct context
				
	EAs_registered 	= event.EAs_registered.order_by('username')
	stylesheet = 'events/event_detail.css'
	script = 'events/event_detail.js'
		
	return render(request, 'events/event_detail.html', {'title':title, 'event':event, 'event_id':event_id, 'registered': request.session['event_registered'], 'EAs_registered':EAs_registered,'event_register_status':event_register_status, 'need':need, 'background_color':background_color,'stylesheet':stylesheet, 'script':script, 'app': app,})

@login_required(login_url='/login/')
def register(request):
	if request.is_ajax():
		event = get_object_or_404(Event, pk = request.session['event_id'])

		registered = request.session['event_registered']
		
		if registered:
			event.EAs_registered.remove(request.user)
			event.save()
			registered = False

		elif not registered:
			if event.EAs_needed <=0:
				registered = False
			else:
				event.EAs_registered.add(request.user)
				event.save()
				registered = True
				
		request.session['event_registered'] = registered
		
		ea = request.user.engineeringambassador
		
		response = json.dumps({"registered":registered, "EAs_needed":event.EAs_needed, "me": str(ea), "me-id":request.user.id, "me-url": ea.picture.url,})
		
		return JsonResponse(response, safe=False)