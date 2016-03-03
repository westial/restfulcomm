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
            content_type='text/plain; charset=utf-8'
        )

    @classmethod
    def POST(cls, data, **kwargs):
        pass

    @classmethod
    def DELETE(cls, data, **kwargs):
        pass