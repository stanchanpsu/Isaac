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
	total_EAs = models.PositiveSmallIntegerField(default = 0, blank = True, null = True)
	EAs_needed = models.PositiveSmallIntegerField(default = 0, blank = True, null = True, editable=False)
	note = models.CharField(max_length = 500, blank = True, null = True, default="No additional notes")
	EAs_registered = models.ManyToManyField(User, related_name= "event", blank = True)
	
	# This allows Event objects to be queried returning instances of the subclasses - documentation: http://django-model-utils.readthedocs.org/en/latest/managers.html#inheritancemanager
	objects = InheritanceManager()
	
	def save(self, *args, **kwargs):
		try:
			self.EAs_needed = self.total_EAs - self.EAs_registered.count()
		except:
			pass
		super(Event, self).save(*args, **kwargs)
	
	# this is somewhat redundant with InheritanceManager, but it is neccessary since I don't have access to the admin code	
	def __unicode__(self):
		if hasattr(self, 'outreachtrip'):
			return self.outreachtrip.__unicode__()
		elif hasattr(self, 'tour'):
			return self.tour.__unicode__()
		elif hasattr(self, 'engrclass'):
			return self.engrclass.__unicode__()
		elif hasattr(self, 'mycoe'):
			return self.mycoe.__unicode__()
		elif hasattr(self, 'freshmanseminar'):
			return self.freshmanseminar.__unicode__()
		else:
			return 'Event'

	
class OutreachTrip(Event):
	school = models.CharField(max_length=30)
	color = "blue"
	shade = "darken-1"
	
	def __unicode__(self):
		return self.school + " Outreach Trip"

		
class Tour(Event):
	tour_types = (('REG','Regular'),('ASP', 'ASP'),('VIP','VIP'),('OTR','Other'))
	tour_type = models.CharField(max_length=3,choices=tour_types,default='regular')
	color = "cyan"
	shade = "darken-1"
	
	def __unicode__(self):
		time = formats.date_format(self.time, "SHORT_TIME")
		return str(self.get_tour_type_display()) + " Tour at " + time


class MyCoe(Event):
	color = "light-blue"
	shade = "darken-1"
	
	def __unicode__(self):
		date = formats.date_format(self.date, "SHORT_DATE")
		return "My COE " + date
	
		
class FreshmanSeminar(Event):
	major = models.CharField(max_length = 40)
	professor = models.CharField(max_length = 40)
	color = "indigo"
	shade = ""
	
	def __unicode__(self):
		return self.major + " Freshman Seminar"
		
		
class ENGRClass(Event):
	veterans = models.BooleanField(default = False)
	color = "deep-purple"
	shade = "darken-1"
	
	def __unicode__(self):
		date = formats.date_format(self.date, "SHORT_DATE")
		return "ENGR Class " + date
		
	class Meta:
		verbose_name_plural = "ENGR classes"