# -*- coding: utf-8 -*-
"""Given a werkzeug http response provide json formatted response result"""

from restfulcomm.core.helpers import HttpHelper
from restfulcomm.services.superbaseservice import BaseService
from restfulcomm.http.jsonresponse import JsonResponse


class HttpResponseToJsonService(BaseService):

    @classmethod
    def run(cls, response):
        """
        :param response: HTTP Response
        :return: JsonResponse
        """
        json_response = cls.factory(response)
        return json_response

    @classmethod
    def factory(cls, response):
        """Return a JsonResponse object by the given Response

        Args:
            response: HTTP Response

        Return:
            JsonResponse
        """
        json_response = JsonResponse()

        if HttpHelper.is_plain_content_type(response.headers['Content-type']):
            json_response.body = response.data.decode('utf-8')
        else:
            json_response.body = response.data

        json_response.status = response.status_code
        json_response.headers = dict(response.headers)

        return json_response
