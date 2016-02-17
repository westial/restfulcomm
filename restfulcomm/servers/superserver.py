"""Super server class"""
from abc import ABCMeta, abstractmethod


class CommServer(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, command_class, configuration):
        """Configures the resource for exit

        Args:
            command_class: ServerCommand class, still not instanced

        Keyword args:
            configuration: Config server configuration object
        """
        self._command_class = command_class
        self._configuration = configuration

    @abstractmethod
    def listen(self):
        """Request the given content to server and return the response"""
        pass
