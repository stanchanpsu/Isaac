from django.contrib import admin

# Register your models here.
from .models import OutreachTrip, Tour, Event, MyCoe, FreshmanSeminar, ENGRClass

admin.site.register(OutreachTrip)
admin.site.register(Tour)
admin.site.register(MyCoe)
admin.site.register(FreshmanSeminar)
admin.site.register(ENGRClass)
