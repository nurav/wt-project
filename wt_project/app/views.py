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
from django.core.urlresolvers import reverse
from django.core.mail import send_mail

from social.backends.google import GooglePlusAuth
from social.backends.utils import load_backends
from social.apps.django_app.utils import psa

from . import models
from .forms import TriggerForm
from eatapp import services

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

@login_required
def trigger_list(request):
    queryset = request.user.triggers.all()
    template_name = "app/trigger_list_item.html"
    return render_to_response(template_name,
        None,
        context_instance=RequestContext(request, { 'object_list': queryset })
        )

@login_required
def trigger_detail(request, pk):
    if request.method == 'GET':
        object = models.Trigger.objects.get(pk=pk)
        template_name = 'app/trigger_detail.html'
        trigger_form = TriggerForm(instance=object)
        return render_to_response(template_name,
            None,
            context_instance=RequestContext(request, 
                { 'form' : trigger_form ,
                 'event' : services.get_event_name_for_id(object.event),
                 'action' : services.get_action_name_for_id(object.action)}
            ))

    if request.method == 'POST':
        object = models.Trigger.objects.get(pk=pk)
        trigger = TriggerForm(request.POST, instance=object)

        trigger.save()

        return HttpResponseRedirect(reverse('trigger-list'))

def index(request):
    if request.user.is_authenticated():
        return render_to_response('app/user_profile.html',
            None,
            context_instance=RequestContext(request))
    else:
        return render_to_response('index.html',
            None,
            context_instance=RequestContext(request))

def profile(request):
    if request.user.is_authenticated():
        return render_to_response('app/user_profile.html',
            None,
            context_instance=RequestContext(request, {
                 'object_list' : request.user.triggers.all()
                }))
    else:
        return render_to_response('index.html',
            None,
            context_instance=RequestContext(request))


class TriggerWizard(SessionWizardView):
    template_name = 'app/new_trigger_wizard.html'

    def done(self, form_list, **kwargs):
        form_data = [form.cleaned_data for form in form_list]

        trigger_event = form_data[0]['select_event']
        trigger_action = form_data[1]['select_action']
        trigger_user = self.request.user
        trigger_original_user = self.request.user
        trigger_description = form_data[2]['description']
        trigger_name = form_data[2]['name']
        trigger_shared = form_data[2]['shared']
        trigger_variable_mapping = form_data[2]['variable_mappings']

        trigger = models.Trigger(
            action=trigger_action,
            event=trigger_event,
            user=trigger_user,
            original_user=trigger_original_user,
            name=trigger_name,
            description=trigger_description,
            shared=trigger_shared,
            variable_mapping=trigger_variable_mapping,
            enabled=True
        )

        trigger.save()

        try:
            send_mail('Trigger Activated', 'Hi, the trigger %s was activated at your account on E.A.T app' % (trigger.name), 'mail@eatapp.com',
    [self.request.user.email], fail_silently=True)
        except:
            print("an error occurred")

        return HttpResponseRedirect(reverse('trigger-success'))

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TriggerWizard, self).dispatch(*args, **kwargs)



			
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

@render_to('about_us.html')
def about_us(request):
    """Login complete view, displays user data"""
    return context()

def shared_triggers(request):
    return render_to_response('app/shared_trigger.html',
        None,
        context_instance=RequestContext(request, 
            { 'object_list': models.Trigger.objects.filter(shared=True) }
        ))
        

def trigger_success(request):
    return render_to_response('app/trigger_success.html',
        None,
        context_instance=RequestContext(request))



