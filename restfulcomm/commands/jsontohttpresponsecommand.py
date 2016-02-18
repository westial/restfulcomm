"""Given a json formatted plain text content return a well formed http
response"""
from restfulcomm.commands.superservercommand import ServerCommand
from restfulcomm.http.jsonresponse import JsonResponse
from werkzeug.wrappers import Response


class JsonToHttpResponseCommand(ServerCommand):
    def __init__(self, raw_content):
        super().__init__(raw_content)
        self._content = JsonResponse.factory(raw_content)

    def execute(self):
        response = self.factory(self._content)
        return response

    @classmethod
    def factory(cls, json_response):
        """Return an Response by the given JsonResponse object

        Args:
            json_response: JsonResponse object

        Return:
            Response
        """
        response = Response(
                response=json_response.body,
                status=json_response.status
        )

        if json_response.headers:

            if 'etag' in json_response.headers:
                response.set_etag(json_response.headers['etag'])

            if 'last_modified' in json_response.headers:
                response.headers.set(
                        'last-modified',
                        json_response.headers['last_modified']
                )

            if 'mimetype_params' in json_response.headers:
                response.mimetype_params.update(
                        json_response.headers['mimetype_params']
                )

            if 'www_authenticate' in json_response.headers:
                response.www_authenticate.update(
                        json_response.headers['www_authenticate']
                )

        return response
