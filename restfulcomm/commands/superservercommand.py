"""Super server command class which operates with the queue server content.
Each project using the restfulcomm should implement its server command, the
action to do with the received data.
"""
from abc import ABCMeta, abstractmethod

from restfulcomm.commands.superbasecommand import BaseCommand


class ServerCommand(BaseCommand, metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, raw_content):
        """Input the raw content from server"""
        self._raw_content = raw_content

    @abstractmethod
    def execute(self):
        """Processes the received data and optionally returns a response"""
        pass
