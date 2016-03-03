# -*- coding: utf-8 -*-
"""Super server endpoint class which defines an action for any request method.
"""
from abc import ABCMeta, abstractmethod


class Endpoint(metaclass=ABCMeta):

    @classmethod
    @abstractmethod
    def GET(cls, *args, **kwargs):
        """GET method request
        :return JsonResponse object
        """
        pass

    @classmethod
    @abstractmethod
    def POST(cls, *args, **kwargs):
        """POST method request
        :return JsonResponse object
        """
        pass

    @classmethod
    @abstractmethod
    def PUT(cls, *args, **kwargs):
        """PUT method request
        :return JsonResponse object
        """
        pass

    @classmethod
    @abstractmethod
    def DELETE(cls, *args, **kwargs):
        """DELETE method request
        :return JsonResponse object
        """
        pass
