# -*- coding: utf-8 -*-
"""Super server endpoint class which defines an action for any request method.
"""


class Endpoint(object):

    @classmethod
    def GET(cls, request, **kwargs):
        """GET method request
        :param request: Request
        :return Response object
        """
        raise NotImplementedError()

    @classmethod
    def POST(cls, request, **kwargs):
        """POST method request
        :param request: Request
        :return Response object
        """
        raise NotImplementedError()

    @classmethod
    def PUT(cls, request, **kwargs):
        """PUT method request
        :param request: Request
        :return Response object
        """
        raise NotImplementedError()

    @classmethod
    def DELETE(cls, request, **kwargs):
        """DELETE method request
        :param request: Request
        :return Response object
        """
        raise NotImplementedError()
