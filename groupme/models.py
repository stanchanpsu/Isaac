from django.db import models
from personal.models import EngineeringAmbassador
from events.models import Event

class group(models.Model):
	group_id = models.PositiveIntegerField(default = 0, blank = True)
	name = models.CharField(max_length = 40)
	image_url = models.CharField(max_length = 100, default = None)
	
	event = models.OneToOneField(Event, default = None, blank = True)
	members = models.ManyToManyField(EngineeringAmbassador, blank = True)	
	
	def __unicode__(self):
		return self.name