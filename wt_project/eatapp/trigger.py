from eatapp import event, action

class Trigger:

    def __init__(self, user, event, action, variable_mappings):
        """event is the event object that will trigger the action(s)
           actions is supposed to be a list of actions that will be triggered 
           by the event
           variable_mappings is of the form: 
            { 'action1' : { 'action_input' : 'event_output' } }
        """   
        self.user = user
        self.event = event
        self.action = action
        self.variable_mappings = variable_mappings

        self.exec_trigger()
        
    def exec_trigger(self):
        """Sets up an event loop that checks whether the trigger should be
           executed, and executes it if that is the case.
        """
        print(str(self.event) + ", " + str(self.action))
        event = self.event
        user = self.user
        if(event.check_for_update(event, user)):
            print(str(self.event) + " successful")
            action = self.action
            action.do(self.variable_mappings, self.user, self.variable_mappings)

    def test_variable_mappings(self):
        """Make sure that all inputs to the action are satisfied, and no 
           inputs are invalid
        """
        raise NotImplementedError


