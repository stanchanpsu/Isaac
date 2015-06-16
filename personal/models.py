from django.db import models
from django.contrib.auth.models import User
# from django.core.validators import RegexValidator

class EngineeringAmbassador(models.Model):
     user = models.OneToOneField(User)
     picture = models.ImageField(blank = True, upload_to = 'profile_pics/')
     rank = models.CharField(max_length = 20, blank = True, default ="Ambassador")
     grad_semester = models.CharField(max_length = 6, blank = True, default="Spring")
     grad_year = models.CharField(max_length = 4, blank = True, default = "2015")
     fall_status = models.BooleanField()
     spring_status = models.BooleanField()
     student_id = models.PositiveIntegerField()
     company_designation = models.CharField(max_length = 20, blank=True)
     companies_worked = models.TextField(blank = True)
     major = models.CharField(max_length = 40)
     major_2 = models.CharField(max_length = 40, blank = True)
     minor = models.CharField(max_length = 40, blank = True)
     minor_2 = models.CharField(max_length = 40, blank = True)
     schreyer_honors = models.BooleanField()
     phone = models.CharField(max_length = 10)
     
     def __unicode__(self):
		return self.user.first_name + ' ' + self.user.last_name
     
