# -*- coding: utf-8 -*-
"""Given a json formatted plain text content provide a werkzeug http response"""
from restfulcomm.services.superbaseservice import BaseService
from restfulcomm.http.jsonresponse import JsonResponse
from werkzeug.datastructures import Headers
from werkzeug.wrappers import Response


class PlainJsonToHttpResponseService(BaseService):

    @classmethod
    def run(cls, plain_json):
        """
        :param plain_json: str
        :return: Response
        """
        json_response = JsonResponse.plain_factory(plain_json)
        response = cls.factory(json_response)
        return response

    @classmethod
    def factory(cls, json_response):
        """Return an Http Response by the given JsonResponse object

        Args:
            json_response: JsonResponse object

        Return:
            Response
        """
        response = Response(
                json_response.body,
                status=json_response.status
        )

        response_headers = Headers()

        while json_response.headers:
            response_headers.add(json_response.headers.popitem())

        response.headers = response_headers

        return response
