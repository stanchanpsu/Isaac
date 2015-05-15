import urllib
from django import forms

class EventView(forms.Form):
	View = forms.ChoiceField(choices=[
	('All','All Events'),('Out','Outreach Trips'),('Tou','Tours')
	], )
	
		
	#def url_args(self):
		#return urllib.urlencode(self.cleaned_data)
