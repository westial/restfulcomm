"""Given a json formatted plain text content provide a werkzeug http response"""
from restfulcomm.services.superbaseservice import BaseService
from restfulcomm.http.jsonresponse import JsonResponse
from werkzeug.wrappers import Response


class JsonToHttpResponseService(BaseService):

    def run(self, plain_json):
        """
        :param plain_json: str
        :return: Response
        """
        json_response = JsonResponse.factory(plain_json)
        response = self.factory(json_response)
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
                status=json_response.status,
                content_type='application/xml'
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
