from eatapp import event, action 
import twitter


class Action(action.Action):
	def get_inputs(self):
		return ['username', 'email']
		
	def do(self, **inputs):
		print(inputs)


class NewTweetAction(action.Action):
	def get_inputs(self):
		return ['username', 'email']
		
	def do(self, **inputs):
		print(inputs)

		
class CreateEvent(event.Event):
	def get_exposed_variables(self):
		return ['event_type', 'post', 'name']
		
	def check_for_update(self):
		return True


EVENTS = {
	('twitter_retweet', 'Retweet a Tweet') : RetweetEvent,
	('twitter_tweet', 'A new Tweet from you') : NewTweetEvent,
}

EVENT_NAMES = list(EVENTS.keys())

ACTIONS = {
	('twitter_retweet', 'Retweet a Tweet') : RetweetAction,
	('twitter_tweet', 'Post new Tweet') : NewTweetAction,
}

ACTION_NAMES = list(ACTIONS.keys())

