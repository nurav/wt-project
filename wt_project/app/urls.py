from django.conf.urls import include, url
from . import views
from . import forms

urlpatterns = [
<<<<<<< HEAD
	url(r'^triggers/$', views.TriggerList.as_view(), name='trigger-list'),
=======
	url(r'^triggers/', views.TriggerList.as_view()),
        url(r'^events/', views.EventList.as_view()),
>>>>>>> f2568786477cbeaffbe2aa30259bc6e3eb0a7a38
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
