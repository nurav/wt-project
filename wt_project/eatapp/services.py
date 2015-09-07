# import eatapp.twitter

SERVICES = {
    'facebook': 'facebook',
    'twitter': 'twitter',
    }

SERVICE_NAMES = [(item, item) for item in SERVICES.keys()]

ACTIONS = {
    'facebook' : {
        'new_post' : 'new_post',
        'new_photo' : 'new_photo',
        },
    'twitter' : {
        'new_tweet' : 'new_tweet',
        'retweet' : 'retweet',
        },
    }