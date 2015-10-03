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
        ACTIONS[(service_name[0], action_name[0])] = action

EVENT_NAMES = []

for service in SERVICES.values():
    for event in service.EVENT_NAMES:
        EVENT_NAMES.append(event)

ACTION_NAMES = []

for service in SERVICES.values():
    for event in service.ACTION_NAMES:
        ACTION_NAMES.append(event)


def get_events_for_user(user):
    providers = []
    for auth in user.social_auth.all():
        providers.append(auth.provider)

    user_events = []
    for event_name in EVENTS.keys():
        service, event_id = event_name
        event_class = EVENTS[(service, event_id)]
        if service in providers:
            user_events.append((event_id, event_class))

    return user_events

def get_actions_for_user(user):
    providers = []
    for auth in user.social_auth.all():
        providers.append(auth.provider)

    user_actions = []
    for event_name in ACTIONS.keys():
        service, action_id = action_name
        action_class = EVENTS[(service, action_id)]
        if service in providers:
            user_events.append((action_id, action_class))

    return user_actions

def get_event_name_for_id(event_id):
    for event_i, event_n in EVENT_NAMES:
        if event_i == event_id:
            return event_n

def get_action_name_for_id(action_id):
    for action_i, action_n in ACTION_NAMES:
        if action_i == action_id:
            return action_n

def get_event_class_for_id(event_id):
    for event_i, event_n in EVENT_NAMES:
        if event_i == event_id:
            return EVENTS[(event_i.split('_')[0], event_i)]

def get_action_class_for_id(action_id):
    for action_i, action_n in ACTION_NAMES:
        if action_i == action_id:
            return ACTIONS[(action_i.split('_')[0], action_i)]