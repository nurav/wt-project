import event, action

class Trigger:

    def __init__(self, event, actions, variable_mappings):
        self.event = event
        self.actions = actions
        self.variable_mappings = variable_mappings

        self.exec_trigger()
        
    def exec_trigger(self):
        while True:
            if(self.event.check_for_update()):
                for action in self.actions:
                    action.do(**self.variable_mappings[action])

    def test_variable_mappings(self):
        raise NotImplementedError


