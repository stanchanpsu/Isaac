from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from events.models import Event
from datetime import date, datetime, timedelta
import time, calendar

month_names = "January February March April May June July August September October November December"
month_names = month_names.split()


@login_required(login_url='/login/')
def month(request, year = time.localtime()[0] , month=time.localtime()[1], change=None):
	year, month = int(year), int(month)
	
	
	#init variables
	cal = calendar.Calendar()
	month_days = cal.itermonthdays(year, month)
	nyear, nmonth, nday = time.localtime()[:3]
	lst = [[]]
	week = 0
	
	# make month lists containing list of days for each week
	# each day tuple will contain list of events and 'current' event indicator
	for day in month_days:
		events = current = False # are there events for this day; current day?
		if day:
			events = Event.objects.filter(date__year=year, date__month=month, date__day=day)
			if day == nday and year == nyear and month == nmonth:
				current = True
				
		lst[week].append((day, events, current))
		if len(lst[week]) == 7:
			lst.append([])
			week += 1
			
	return render(request, 'cal/calendar.html', {'year':year, 'month':month, 'month_days':lst, 'month_name': month_names[month-1],})
