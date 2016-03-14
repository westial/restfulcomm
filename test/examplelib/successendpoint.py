# -*- coding: utf-8 -*-
"""Example endpoint for parameters printing"""
from restfulcomm.http.superendpoint import Endpoint
from werkzeug.wrappers import Response


class SuccessEndpoint(Endpoint):

    @classmethod
    def GET(cls, request, **kwargs):
        content = kwargs['content']
        return Response(
            response=content,
            content_type='text/plain'
        )

