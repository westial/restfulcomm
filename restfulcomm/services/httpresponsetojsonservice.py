# -*- coding: utf-8 -*-
"""Given a werkzeug http response provide json formatted plain text"""
from restfulcomm.services.superbaseservice import BaseService
from restfulcomm.http.jsonresponse import JsonResponse


class HttpResponseToJsonService(BaseService):

    def run(self, response):
        """
        :param response: Response
        :return: str
        """
        json_response = self.factory(response)
        return json_response.to_json()

    @classmethod
    def factory(cls, response):
        """Return an Response by the given JsonResponse object

        Args:
            response: Response object

        Return:
            JsonResponse
        """
        json_response = JsonResponse()
        json_response.body = response.data
        json_response.status = response.status_code
        json_response.headers = response.headers.to_list()

        return json_response
