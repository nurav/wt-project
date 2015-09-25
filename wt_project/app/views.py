from django.views import generic
from app_api import models
from django.contrib.auth import views
from django.shortcuts import render_to_response

class TriggerList(generic.ListView):
    model = models.Trigger
    template_name = "app/trigger_list_item.html"
    paginate_by = 3

def index(request):
    pass

def profile(request):
    pass

def event_list(request):
    return render_to_response('app/event_list.html',
                              None,
                              context=RequestContext(request))
