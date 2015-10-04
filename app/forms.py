from django import forms
from django.forms import ModelForm
from app.models import Trigger
from eatapp.services import EVENT_NAMES, ACTION_NAMES
from eatapp import services

class SelectEventForm(forms.Form):
	"""Select event"""
	select_event = forms.ChoiceField(
		choices=EVENT_NAMES, 
		widget=forms.RadioSelect,
		label="Select an event:"
	)

	class Media:
		css = {
			'all': ()
		}
			


class SelectActionForm(forms.Form):
	"""Select action"""
	select_action = forms.ChoiceField(
		choices=ACTION_NAMES,
		widget=forms.RadioSelect,
		label="Select an action"
	)


class TriggerDescriptionForm(forms.Form):
	"""docstring for TriggerDescriptionForm"""
	name = forms.CharField()
	description = forms.CharField(widget=forms.Textarea, required=False)
	variable_mappings = forms.CharField(label='Inputs to action', widget=forms.Textarea, required=True)
	shared = forms.BooleanField(required=False)


class TriggerForm(ModelForm):
	class Meta:
		model = Trigger
		fields = ['name', 'description', 'shared', 'enabled', 'variable_mapping']
		

