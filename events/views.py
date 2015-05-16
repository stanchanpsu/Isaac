from django.shortcuts import render
from django.http import HttpResponse

from .models import OutreachTrip,Tour
from .forms import EventView

# Create your views here.

def list_events(request):
	
	title = 'EA events'
	
	# get selection from event_view dropdown
	event_view = request.GET.get('event_view', False)			
	
	outreach_list = OutreachTrip.objects.order_by('date')
	tour_list = Tour.objects.order_by('date')
	
	return render(request,'events/list_events.html', {'outreach_list':outreach_list, 'tour_list':tour_list, 'event_view': event_view, 'title':title,})


def event_detail(request, event_type, event_id):
	
	return HttpResponse("this is %s of %s" % (event_id, event_type))
