from django.db import models
from django import forms

# Create your models here.

class OutreachTrip(models.Model):
	school = models.CharField(max_length=30)
	date = models.DateField()
	hours = models.DecimalField(max_digits=3,decimal_places=1)
	location = models.CharField(max_length = 140)
	EAs_needed = models.PositiveSmallIntegerField()
	note = models.CharField(max_length = 500, blank = True, null = True)
	
	def __unicode__(self):
		return self.school
		
class Tour(models.Model):
	tour_types = (('REG','Regular'),('ASP', 'ASP'),('VIP','VIP'),('OTH','Other'))
	tour_type = models.CharField(max_length=3,choices=tour_types,default='reg')
	date = models.DateField()
	time = models.TimeField()
	hours = models.DecimalField(max_digits=3, decimal_places=1)
	location = models.CharField(max_length=30)
	EAs_needed = models.PositiveSmallIntegerField()
	note = models.CharField(max_length = 500, blank = True, null = True)
	
	def __unicode__(self):
		return str(self.date) + " " + self.tour_type + " " + str(self.time)
	

