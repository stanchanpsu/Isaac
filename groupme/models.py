from django.db import models
from personal.models import EngineeringAmbassador
from events.models import Event

class Group(models.Model):
	group_id = models.CharField(max_length = 20, default = 0, blank = True)
	name = models.CharField(max_length = 40, blank = True)
	image_url = models.CharField(max_length = 100, default = None, blank = True)
	
	event = models.OneToOneField(Event, default = None, blank = True)
	members = models.ManyToManyField(EngineeringAmbassador, blank = True)	
	
	def __unicode__(self):
		return self.name