from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from events.models import Event
from datetime import date, datetime, timedelta
import time, calendar

app = "calendar"
title = "Calendar"
stylesheet = "cal/calendar.css"


month_names = "January February March April May June July August September October November December"
month_names = month_names.split()

@login_required(login_url='/login/')
def year(request, year = None):
	if year: year = int(year)
	else: year = time.localtime()[0]
	
	current_year, current_month = time.localtime()[:2]
	
	fall = month_names[6:]
	spring = month_names[:6]
	
	return render(request, 'cal/year.html', {'app':app, 'title':title, 'stylesheet':stylesheet, 'year':year, 'fall':fall, 'spring':spring, 'current_year':current_year,'current_month':current_month,})

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
			
	return render(request, 'cal/month.html', {'app':app, 'title':title, 'stylesheet':stylesheet, 'year':year, 'month':month, 'month_days':lst, 'month_name': month_names[month-1],})
