import abc

class Event:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_exposed_variables(self):
        """Returns a map of variables and their types
        """
        return

    @abc.abstractmethod
    def check_for_update(self):
        """Adds a hook to the event_listener
           TODO: Add meaningful documentation
        """
        return
 

