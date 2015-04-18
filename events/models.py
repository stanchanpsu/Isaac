from django.db import models

# Create your models here.

class Event(models.Model):
	event = models.CharField(max_length=30)
	date = models.DateField()
	time = models.TimeField()
	hours = models.DecimalField(max_digits=4,decimal_places=2)
	location = models.CharField(max_length = 140)
	EAs_needed = models.PositiveSmallIntegerField()
	description = models.CharField(max_length = 500)
	
	def __unicode__(self):
		return self.event
	
