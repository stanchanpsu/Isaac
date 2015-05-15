from django.contrib import admin

# Register your models here.
from .models import OutreachTrip, Tour

admin.site.register(OutreachTrip)
admin.site.register(Tour)
