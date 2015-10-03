from redis import Redis
from rq import Queue
from django.contrib.auth.models import User
import time
import threading

from app import models
from eatapp import services
from eatapp.trigger import Trigger

#q = Queue(connection=Redis())

from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    args = '<poll_id poll_id ...>'
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        thread = threading.Thread(target=exec_service, args=(), kwargs={})
        thread.start()
                    
def exec_service():
    for trigger_data in models.Trigger.objects.all():
        print("new trigger run")
        trigger = Trigger(
                user=trigger_data.user,
                event=services.get_event_class_for_id(trigger_data.event),
                action=services.get_action_class_for_id(trigger_data.action),
                variable_mappings=trigger_data.variable_mapping
            )
        thread = threading.Thread(target=trigger.exec_trigger, args=(), kwargs={})
        thread.start()
    time.sleep(90)


if __name__ == '__main__':
    exec_service()

#result = q.enqueue(exec_service)



