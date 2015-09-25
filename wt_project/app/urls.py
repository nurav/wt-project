from django.conf.urls import include, url
from . import views

urlpatterns = [
    url('', views.TriggerList.as_view()),
    url('^events/', views.event_list),
]