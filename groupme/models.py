from django.db import models

class group(models.Model):
	name = models.CharField(max_length = 40)
	groupme_id = models.PositiveIntegerField()

	def __unicode__(self):
		return self.name