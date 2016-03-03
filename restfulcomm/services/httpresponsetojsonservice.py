# -*- coding: utf-8 -*-
"""Given a werkzeug http response provide json formatted response result"""
from restfulcomm.services.superbaseservice import BaseService
from restfulcomm.http.jsonresponse import JsonResponse


class HttpResponseToJsonService(BaseService):

    @classmethod
    def run(cls, response):
        """
        :param response: Response
        :return: JsonResponse
        """
        json_response = cls.factory(response)
        return json_response

    @classmethod
    def factory(cls, response):
        """Return an Response by the given JsonResponse object

        Args:
            response: Response object

        Return:
            JsonResponse
        """
        json_response = JsonResponse()
        json_response.body = response.data.decode('utf-8')
        json_response.status = response.status_code
        json_response.headers = response.headers.to_list()

        return json_response
