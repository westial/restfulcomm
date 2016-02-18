"""Example command for parameters response"""
from restfulcomm.commands.superservercommand import ServerCommand
from restfulcomm.http.jsonresponse import JsonResponse


class ConvertJsonToResponseCommand(ServerCommand):

    def __init__(self, raw_content):
        super().__init__(raw_content)
        json_response = JsonResponse()
        json_response.body = raw_content.decode('utf-8')
        json_response.status = 200
        self._content = json_response.to_json()

    def execute(self):
        return self._content
