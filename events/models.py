from django.db import models
from django import forms
from django.contrib.auth.models import User

# Create your models here.

class Event(models.Model):
	time = models.TimeField()
	date = models.DateField()
	hours = models.DecimalField(max_digits=3,decimal_places=1, blank = True, null = True)
	location = models.CharField(max_length = 140, blank = True, null = True)
	EAs_needed = models.PositiveSmallIntegerField(blank = True, null = True)
	note = models.CharField(max_length = 500, blank = True, null = True)
	
class OutreachTrip(Event):
	school = models.CharField(max_length=30)
	EAs_registered = models.ManyToManyField(User, related_name = 'outreach', blank = True)
	
	def __unicode__(self):
		return self.school
		
class Tour(Event):
	tour_types = (('REG','Regular'),('ASP', 'ASP'),('VIP','VIP'),('OTR','Other'))
	tour_type = models.CharField(max_length=3,choices=tour_types,default='regular')
	EAs_registered = models.ManyToManyField(User, related_name = 'tours', blank = True)
	
	def __unicode__(self):
		return str(self.date) + " " + self.tour_type + " " + str(self.time)
