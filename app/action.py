import abc

class Action:

    @abc.abstractmethod
    def get_inputs(self):
        return

    @abc.abstractmethod
    def do(self, **inputs):
        return
