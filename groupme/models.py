from django.db import models
from personal.models import EngineeringAmbassador
from events.models import Event
from django.dispatch import receiver
from django.db.models.signals import post_delete
from django.shortcuts import get_object_or_404

class Group(models.Model):
	group_id = models.CharField(max_length = 20, default = 0, blank = True)
	name = models.CharField(max_length = 40, blank = True)
	image_url = models.CharField(max_length = 100, default = None, blank = True, null = True)
	
	event = models.OneToOneField(Event, default = None, blank = True, null = True)
	members = models.ManyToManyField(EngineeringAmbassador, blank = True)	
	
	def __unicode__(self):
		return self.name
		
@receiver(post_delete, sender=Event)
def delete_Group(sender, **kwargs):
	event = kwargs.get('instance')
	if hasattr(event, "group"):
		group = get_object_or_404(Group, event = event)
		group.delete()