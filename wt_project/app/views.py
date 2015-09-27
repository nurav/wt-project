from functools import wraps

from django.views import generic
from django.http import HttpResponseRedirect
from django.contrib.auth import views
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from formtools.wizard.views import SessionWizardView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.template import RequestContext
from django.conf import settings

from social.backends.google import GooglePlusAuth
from social.backends.utils import load_backends
from social.apps.django_app.utils import psa

from . import models

def render_to(tpl):
    def decorator(func):
        @wraps(func)
        def wrapper(request, *args, **kwargs):
            out = func(request, *args, **kwargs)
            if isinstance(out, dict):
                out = render_to_response(tpl, out, RequestContext(request))
            return out
        return wrapper
    return decorator

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
		   context_instance=RequestContext(request))

def event_list(request):
    return render_to_response('app/event_list.html',
        None,
        context_instance=RequestContext(request))


class TriggerWizard(SessionWizardView):
	template_name = 'app/new_trigger_wizard.html'

	def done(self, form_list, **kwargs):
		trigger_event = ''
		# trigger_action = ''
		# trigger_user = ''
		# trigger_original_user = ''
		# trigger_variable_mapping = ''
		# for form in form_list:
		# 	pass

			
def context(**extra):
    return dict({
        'plus_id': getattr(settings, 'SOCIAL_AUTH_GOOGLE_PLUS_KEY', None),
        'plus_scope': ' '.join(GooglePlusAuth.DEFAULT_SCOPE),
        'available_backends': load_backends(settings.AUTHENTICATION_BACKENDS)
    }, **extra)


@render_to('app/service-home.html')
def home(request):
    """Home view, displays login mechanism"""
    if request.user.is_authenticated():
        return redirect('services-done')
    return context()


@login_required
@render_to('app/service-home.html')
def done(request):
    """Login complete view, displays user data"""
    return context()



