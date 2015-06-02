from django.db import models
from django.contrib.auth.models import User
# from django.core.validators import RegexValidator

class EngineeringAmbassador(models.Model):
     user = models.OneToOneField(User)
     picture = models.ImageField()
     grad_date = models.DateField()
     fall_status = models.BooleanField()
     spring_status = models.BooleanField()
     student_id = models.PositiveIntegerField()
     company_designation = models.CharField(max_length = 20)
     major = models.CharField(max_length = 20)
     major_2 = models.CharField(max_length = 20)
     minor = models.CharField(max_length = 20)
     minor_2 = models.CharField(max_length = 20)
     schreyer_honors = models.BooleanField()
     phone = models.CharField(max_length = 10)
     
     
