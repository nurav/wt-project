from . import twitter

SERVICES = {
    ('twitter', 'Twitter'): twitter,
    }

SERVICE_NAMES = SERVICES.keys()

EVENTS = {}

for service_name, service in SERVICES.items():
    for event_name, event in service.EVENTS.items():
        EVENTS[(service_name[0], event_name[0])] = event

ACTIONS = {}

for service_name, service in SERVICES.items():
    for action_name, action in service.ACTIONS.items():
        EVENTS[(service_name[0], action_name[0])] = action

EVENT_NAMES = []

for service in SERVICES.values():
    for event in service.EVENT_NAMES:
        EVENT_NAMES.append(event)

ACTION_NAMES = []

for service in SERVICES.values():
    for event in service.ACTION_NAMES:
        ACTION_NAMES.append(event)