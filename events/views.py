from django.shortcuts import render

from .models import Event

# Create your views here.

def list_events(request):
	event_list = Event.objects.order_by('-date')
	return render(request,'events/list_events.html', {'event_list':event_list})
