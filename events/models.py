from django.db import models
from django import forms
from django.contrib.auth.models import User
from model_utils.managers import InheritanceManager

#date formatting
from django.utils import formats

class Event(models.Model):
	time = models.TimeField()
	date = models.DateField()
	hours = models.DecimalField(max_digits=3,decimal_places=1, blank = True, null = True, default=0)
	location = models.CharField(max_length = 140, blank = True, null = True)
	EAs_needed = models.PositiveSmallIntegerField(default = 0, blank = True, null = True)
	note = models.CharField(max_length = 500, blank = True, null = True, default="No additional notes")
	
	# This allows Event objects to be queried returning instances of the subclasses - documentation: http://django-model-utils.readthedocs.org/en/latest/managers.html#inheritancemanager
	objects = InheritanceManager()
	
	def __unicode__(self):
		if hasattr(self, 'outreachtrip'):
			return self.outreachtrip.__unicode__()
		elif hasattr(self, 'tour'):
			return self.tour.__unicode__()
		else:
			return 'Event'
	
class OutreachTrip(Event):
	school = models.CharField(max_length=30)
	EAs_registered = models.ManyToManyField(User, related_name = 'outreach', blank = True)
	
	def __unicode__(self):
		return self.school
		
	def detail_url(self):
		return "outreach/" + str(self.id)
		
class Tour(Event):
	tour_types = (('REG','Regular'),('ASP', 'ASP'),('VIP','VIP'),('OTR','Other'))
	tour_type = models.CharField(max_length=3,choices=tour_types,default='regular')
	EAs_registered = models.ManyToManyField(User, related_name = 'tours', blank = True)
	
	def __unicode__(self):
		time = formats.date_format(self.time, "SHORT_TIME")
		return self.tour_type + " " + time + " Tour"
		
	def detail_url(self):
		return "tour/" + str(self.id)
	
class Class(Event):
	veterans = models.BooleanField(default = False)
	
	def __unicode__(self):
		date = formats.date_format(self.date, "SHORT_DATE")
		return "ENGR Class " + date
		
	class Meta:
		verbose_name_plural = "classes"

class MyCoe(Event):
	def __unicode__(self):
		date = formats.date_format(self.date, "SHORT_DATE")
		return "MyCOE " + date
		
class FreshmanSeminar(Event):
	major = models.CharField(max_length = 40)
	professor = models.CharField(max_length = 40)
	def __unicode__(self):
		return self.major + " Freshman Seminar"