from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from events.models import Event
from datetime import date, datetime, timedelta
import time, calendar, collections

app = "calendar"
title = "Calendar"

month_names = "January February March April May June July August September October November December"
month_names = month_names.split()

@login_required(login_url='/login/')
def year(request, year = None):
	if year: year = int(year)
	else: year = time.localtime()[0]
	
	current_year, current_month = time.localtime()[:2]
	stylesheet = "cal/year.css"

	fall = collections.OrderedDict()
	spring = collections.OrderedDict()
	
	for month in range(7,13):
		events = Event.objects.filter(date__year=year, date__month=month).count()
		month_name = (month_names[month-1])	
		fall[month_name] = events
		
	for month in range(1,7):
		events = Event.objects.filter(date__year=year, date__month=month).count()
		month_name = (month_names[month-1])	
		spring[month_name] = events
	
	return render(request, 'cal/year.html', {'app':app, 'title':title, 'stylesheet':stylesheet, 'year':year, 'fall':fall, 'spring':spring, 'current_year':current_year,'current_month':current_month, 'month_names': month_names})

@login_required(login_url='/login/')
def month(request, year = time.localtime()[0] , month=time.localtime()[1], change=None):
	year, month = int(year), int(month)
	
	
	#init variables
	stylesheet = "cal/month.css"
	cal = calendar.Calendar()
	month_days = cal.itermonthdays(year, month)
	nyear, nmonth, nday = time.localtime()[:3]
	lst = [[]]
	week = 0
	previous_month = month_names[month-2]
	current_month = month_names[month-1]
	next_month = month_names[month%12] #remember python lists are zero indexed
	
	
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
			
	return render(request, 'cal/month.html', {'app':app, 'title':title, 'stylesheet':stylesheet, 'year':year, 'month':month, 'month_days':lst, 'previous_month':previous_month,'current_month':current_month,'next_month':next_month,})
