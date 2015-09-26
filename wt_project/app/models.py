from django.db import models
from eatapp.services import SERVICE_NAMES

class APIAuthenticationKey(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('auth.User', related_name='api_auth_keys')
    service = models.CharField(choices=SERVICE_NAMES, max_length=20)
    auth_data = models.TextField()
    
    class Meta:
        unique_together = (('user', 'service'),)
        

class Trigger(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('auth.User', related_name='triggers')
    original_user = models.ForeignKey('auth.User', related_name='created_trigger')
    action = models.CharField(max_length=50)
    event = models.CharField(max_length=50)
    script = models.TextField()
    shared = models.BooleanField()
    enabled = models.BooleanField()
    name = models.CharField(max_length=100, blank=False)
