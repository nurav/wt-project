from eatapp import event, action, trigger

class TwitterAction(action.Action):
	def get_inputs(self):
		return ['username', 'email']
		
	def do(self, **inputs):
		print(inputs)
		
class TwitterPostEvent(event.Event):
	def get_exposed_variables(self):
		return ['post', 'name']
		
	def check_for_update(self):
		return True

event = TwitterPostEvent()
action = TwitterAction()
variable_mapping = { action: { 'name': 'username' }}
trigger = trigger.Trigger(event, [action], variable_mapping)

