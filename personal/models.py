from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
# from django.core.validators import RegexValidator

class EngineeringAmbassador(models.Model):
     user = models.OneToOneField(User)
     picture = models.ImageField(blank = True, upload_to = 'profile_pics/')
     rank = models.CharField(max_length = 20, blank = True, default ="Ambassador")
     aboutme = models.TextField(max_length = 500, blank = True)
     grad_semester = models.CharField(max_length = 6, blank = True, default="Spring")
     grad_year = models.CharField(max_length = 4, blank = True, default = "2015")
     fall_status = models.BooleanField(default=True)
     spring_status = models.BooleanField(default=True)
     student_id = models.PositiveIntegerField(blank = True, null=True)
     company_designation = models.CharField(max_length = 20, blank=True)
     companies_worked = models.TextField(blank = True)
     major = models.CharField(blank=True, max_length = 40)
     major_2 = models.CharField(max_length = 40, blank = True)
     minor = models.CharField(max_length = 40, blank = True)
     minor_2 = models.CharField(max_length = 40, blank = True)
     schreyer_honors = models.BooleanField(default = False)
     phone = models.CharField(max_length = 10, blank=True)
     groupme_id = models.CharField(max_length = 20, blank=True, null=True)
     
     def __unicode__(self):
		return self.user.first_name + ' ' + self.user.last_name
     
@receiver(post_save, sender=User)
def create_EngineeringAmbassador(sender, **kwargs):
    if kwargs.get('created', False):
        EngineeringAmbassador.objects.get_or_create(user=kwargs.get('instance'))