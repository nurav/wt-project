from django.conf.urls import include, url
from . import views
from . import forms

urlpatterns = [
	url(r'^triggers/$', views.TriggerList.as_view(), name='trigger-list'),
 	url(r'^$', 'app.views.index', name='index'),
    url(r'^accounts/profile', 'app.views.profile', name='profile'),
    url('^events/', views.event_list),
    url('triggers/new/$', views.TriggerWizard.as_view([
    		forms.SelectEventForm,
    		forms.SelectActionForm,
    		forms.TriggerDescriptionForm,
    	]), name='new-trigger-wizard'
    )
]
