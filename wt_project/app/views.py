from django.views import generic
from . import models
from django.http import HttpResponseRedirect
from django.contrib.auth import views
from django.shortcuts import render_to_response
from formtools.wizard.views import SessionWizardView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class TriggerList(generic.ListView):
    model = models.Trigger
    template_name = "app/trigger_list_item.html"
    paginate_by = 3

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TriggerList, self).dispatch(*args, **kwargs)

def index(request):
    pass

def profile(request):
    if request.user.is_authenticated():
    	return render_to_response('app/user_profile.html',
    							   None,
    							   context=RequestContext)

def event_list(request):
    return render_to_response('app/event_list.html',
                              None,
                              context=RequestContext(request))


class TriggerWizard(SessionWizardView):
	template_name = 'app/new_trigger_wizard.html'

	def done(self, form_list, **kwargs):
		super(ClassName, self).__init__()
		self.arg = arg
		


