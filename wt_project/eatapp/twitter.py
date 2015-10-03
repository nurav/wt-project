from eatapp import event, action 
import tweepy
from tweepy.error import TweepError
from django.contrib.auth.models import User
import social.apps.django_app.default
import sys

consumer_token = 'WCSRVJPnIGn4o9vsuC7XvSb27'
consumer_secret = 'ZCkGxKw8KAMuAM2aLRTdII7oJUtA1rH6hmeCeSO1XgXZOnpdLO'

class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print (status)
        return False

    def on_error(self, status_code):
        print (status_code)
        return True # Don't kill the stream

    def on_timeout(self):
        print ('Timeout...')
        return True # Don't kill the stream

def get_api(user):
    for auth in User.objects.get(username=user).social_auth.all():
        if auth.provider == 'twitter':
            social_auth = auth.extra_data
    token = social_auth['access_token']['oauth_token']
    secret = social_auth['access_token']['oauth_token_secret']
    auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
    auth.set_access_token(token, secret)
    api = tweepy.API(auth)

    return api

def is_tweet_from_user(tweet, user):
    if tweet['from_user_id'] == user:
        return True
    return False


class RetweetAction(action.Action):
    def get_inputs(self):
        return ['username', 'email']
        
    def do(self, user, inputs):
        print("retweet action activated")
        try:
            api = get_api(user)
            tweet = api.update_status(status=inputs)
        except TweepError as e:
            print(e)



class NewTweetAction(action.Action):
    def get_inputs(self):
        return ['username', 'email']
        
    def do(self, user, inputs):
        print("retweet action activated")
        try:
            api = get_api(user)
            tweet = api.update_status(status=inputs)
        except TweepError as e:
            print(e)
            

        
class RetweetEvent(event.Event):
    def get_exposed_variables(self):
        return ['post', 'name']
        
    def check_for_update(self, user):
        for auth in User.objects.get(username=user).social_auth.all():
            if auth.provider == 'twitter':
                username = auth.extra_data['access_token']['screen_name']
        api = get_api(user)
        # tweets = api.search('#eatapp')
        # for tweet in tweets:
        #     if tweet.user.name == username:
        #         return True
        # return True

        myStreamListener = MyStreamListener()
        myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
        myStream.filter(track=['eatapp'])
        return True

class NewTweetEvent(event.Event):
    def get_exposed_variables(self):
        return ['post', 'name']
        
    def check_for_update(self, user):
        for auth in User.objects.get(username=user).social_auth.all():
            if auth.provider == 'twitter':
                username = auth.extra_data['access_token']['screen_name']
        api = get_api(user)
        # tweets = api.search('#eatapp')
        # for tweet in tweets:
        #     if tweet.user.name == username:
        #         return True
        # return True

        myStreamListener = MyStreamListener()
        myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
        myStream.filter(track=['eatapp'])
        return True

EVENTS = {
    ('twitter_retweet', 'Twitter: Retweet a Tweet') : RetweetEvent,
    ('twitter_tweet', 'Twitter: A new Tweet from you') : NewTweetEvent,
}

EVENT_NAMES = list(EVENTS.keys())

ACTIONS = {
    ('twitter_retweet', 'Twitter: Retweet a Tweet') : RetweetAction,
    ('twitter_tweet', 'Twitter: Post new Tweet') : NewTweetAction,
}

ACTION_NAMES = list(ACTIONS.keys())

