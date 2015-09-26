from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^triggers/', views.TriggerList.as_view()),
 	url(r'^$', 'app.views.index', name='index'),
    url(r'^accounts/profile', 'app.views.profile', name='profile'),
    url('', views.TriggerList.as_view()),
    url('^events/', views.event_list),
]
