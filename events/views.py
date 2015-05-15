from django.shortcuts import render
from django.http import HttpResponse

from .models import OutreachTrip,Tour
from .forms import EventView

# Create your views here.

def list_events(request):
	
	# get selection from event_view dropdown
	event_view = request.GET.get('event_view', False)
	
	# pass in value as preselected dropdown THIS NEEDS TO BE FIXED
	if event_view is "out":
		out_selected = "selected"
		all_selected, tour_selected = '  '
	elif event_view is "tour":
		tour_selected = "selected"
		all_selected, out_selected = '  '
	else:
		all_selected = "selected"
		out_selected, tour_selected = '  '
			
	
	outreach_list = OutreachTrip.objects.order_by('date')
	tour_list = Tour.objects.order_by('date')
	
	return render(request,'events/list_events.html', {'outreach_list':outreach_list, 'tour_list':tour_list, 'all_selected': all_selected, 'out_selected': out_selected, 'tour_selected': tour_selected})


def event_detail(request, event_type, event_id):
	
	return HttpResponse("this is %s of %s" % (event_id, event_type))
