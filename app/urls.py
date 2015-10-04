from django.conf.urls import include, url
from . import views
from . import forms

urlpatterns = [
	 url(r'^triggers/shared/$', views.shared_triggers, name='shared-trigger-list'),
	url(r'^triggers/$', views.trigger_list, name='trigger-list'),
 	url(r'^$', 'app.views.index', name='index'),
    url(r'^accounts/profile', 'app.views.profile', name='profile'),
    url('^welcome/', views.welcome),
    url('^trigger_success/', views.trigger_success),
    url('triggers/new/$', views.TriggerWizard.as_view([
    		forms.SelectEventForm,
    		forms.SelectActionForm,
    		forms.TriggerDescriptionForm,
    	]), name='new-trigger-wizard'
    ),
    url(r'^triggers/(?P<pk>[0-9]*)/$', views.trigger_detail, name='trigger-detail'),
    url(r'^services/$', views.home, name='services-home'),
    url(r'^done/$', views.done, name='services-done'),
    url(r'^triggers/success/$', views.trigger_success, name='trigger-success'),
	url(r'^about_us/$', views.about_us, name='about-us'),
]
