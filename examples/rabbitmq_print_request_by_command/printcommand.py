"""Example command for parameters printing"""

from restfulcomm.commands.superservercommand import ServerCommand


class PrintCommand(ServerCommand):

    def __init__(self, raw_content):
        super().__init__(raw_content)
        self._content = raw_content

    def execute(self):
        print(self._content)
