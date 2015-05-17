import urllib
from django import forms

class EventView(forms.Form):
	View = forms.ChoiceField(choices=[
	('All','All Events'),('Out','Outreach Trips'),('Tou','Tours')
	], )
