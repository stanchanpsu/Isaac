from django.db import models
from django.contrib.auth.models import User

class EngineeringAmbassador(models.Models):
     user = models.OneToOneField(User)
     picture = models.PictureField
     
