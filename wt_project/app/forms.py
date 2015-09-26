from django import forms
from eatapp.services import EVENT_NAMES

class SelectEventForm(forms.Form):
	"""Select event"""
	events_list = forms.ChoiceField(choices=EVENT_NAMES)


class SelectActionForm(forms.Form):
	"""Select action"""
	actions_list = forms.ChoiceField(choices=EVENT_NAMES)


class TriggerDescriptionForm(forms.Form):
	"""docstring for TriggerDescriptionForm"""
	name = forms.CharField()
	description = forms.CharField(required=False)
	shared = forms.BooleanField(required=False)
		

