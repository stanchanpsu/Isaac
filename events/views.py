from django.shortcuts import render
from django.http import HttpResponse

from .models import OutreachTrip,Tour

# Create your views here.

def list_events(request):
	outreach_list = OutreachTrip.objects.order_by('date')
	tour_list = Tour.objects.order_by('date')
	return render(request,'events/list_events.html', {'outreach_list':outreach_list, 'tour_list':tour_list})

def event_detail(request, event_type, event_id):
	
	return HttpResponse("this is %s of %s" % (event_id, event_type))
