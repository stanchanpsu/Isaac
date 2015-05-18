from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


from .models import OutreachTrip,Tour
from .forms import EventView


@login_required(login_url='/login/')
def list_events(request):
		
	title = 'EA events'
	
	# get selection from event_view dropdown
	event_view = request.GET.get('event_view', False)			
	
	outreach_list = OutreachTrip.objects.order_by('date')
	tour_list = Tour.objects.order_by('date')
	
	return render(request,'events/list_events.html', {'outreach_list':outreach_list, 'tour_list':tour_list, 'event_view': event_view, 'title':title,})	
	

@login_required(login_url='/login/')
def event_detail(request, event_type, event_id):
		
	if event_type == 'outreach':
		event = get_object_or_404(OutreachTrip, pk = event_id)
		title = event.school + ' Outreach Trip'
		descript = 'School'
		descript_field = event.school
	elif event_type == 'tour':
		event = get_object_or_404(Tour, pk = event_id)
		title = str(event.time) + ' ' + event.tour_type + ' Tour on ' + str(event.date)
		descript = 'Time'
		descript_field = event.time

## figure this out		
	if request.POST:
		user = request.user
		event.EAs_registered.add(user)
		
		
		
	return render(request, 'events/event_detail.html', {'title':title, 'event':event, 'descript':descript, 'descript_field':descript_field,'event_type':event_type, 'event_id':event_id,})
