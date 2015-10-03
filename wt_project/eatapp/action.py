import abc

class Action:
    """An abstract class that all actions will implement
    """

    @abc.abstractmethod
    def get_inputs(self):
        """All inputs to the action in a list
        """
        return

    @abc.abstractmethod
    def do(self, user, **inputs):
        """Executes the action
        """
        return
