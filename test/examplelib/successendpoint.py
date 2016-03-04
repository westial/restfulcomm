# -*- coding: utf-8 -*-
"""Example command for parameters printing"""
from restfulcomm.http.superendpoint import Endpoint
from werkzeug.wrappers import Response


class SuccessEndpoint(Endpoint):

    @classmethod
    def PUT(cls, data, **kwargs):
        pass

    @classmethod
    def GET(cls, data, content):
        return Response(
            response=content,
            content_type='application/json'
        )

    @classmethod
    def POST(cls, data, **kwargs):
        pass

    @classmethod
    def DELETE(cls, data, **kwargs):
        pass