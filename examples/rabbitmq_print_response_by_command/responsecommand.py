"""Example command for parameters response"""
from restfulcomm.commands.superservercommand import ServerCommand


class ResponseCommand(ServerCommand):

    def __init__(self, raw_content):
        super().__init__(raw_content)
        self._content = raw_content.decode("utf-8")

    def execute(self):
        return self._content
