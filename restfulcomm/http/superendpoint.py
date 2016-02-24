# -*- coding: utf-8 -*-
"""Super server endpoint class which defines an action for any request method.
"""
from abc import ABCMeta, abstractmethod


class Endpoint(metaclass=ABCMeta):

    @classmethod
    @abstractmethod
    def GET(cls, **kwargs):
        """GET method request

        Keyword args:
            kwargs: url parameters

        Return:
            JsonResponse object
        """
        pass

    @classmethod
    @abstractmethod
    def POST(cls, data, **kwargs):
        """POST method request

        Args:
            data: dict data fields

        Keyword args:
            kwargs: url parameters

        Return:
            JsonResponse object
        """
        pass

    @classmethod
    @abstractmethod
    def PUT(cls, data, **kwargs):
        """PUT method request

        Args:
            data: dict data fields

        Keyword args:
            kwargs: url parameters

        Return:
            JsonResponse object
        """
        pass

    @classmethod
    @abstractmethod
    def DELETE(cls, **kwargs):
        """DELETE method request

        Keyword args:
            kwargs: url parameters

        Return:
            JsonResponse object
        """
        pass
