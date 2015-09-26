from . import twitter

SERVICES = {
    ('twitter', 'Twitter') : twitter,
    }

SERVICE_NAMES = SERVICES.keys()

EVENT_NAMES = []

for service in SERVICES.values():
    for event in service.EVENT_NAMES:
        EVENT_NAMES.append(event)

ACTION_NAMES = []

for service in SERVICES.values():
    for event in service.ACTION_NAMES:
        EVENT_NAMES.append(event)