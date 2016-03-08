# -*- coding: utf-8 -*-
"""Super client class"""
from abc import ABCMeta, abstractmethod


class CommClient(metaclass=ABCMeta):

    METHOD_GET = 'GET'
    METHOD_POST = 'POST'
    METHOD_PUT = 'PUT'
    METHOD_DELETE = 'DELETE'

    @abstractmethod
    def __init__(self, configuration):
        """Configures the request components and initializes the instance.

        Args:
            configuration: Config server configuration object
        """
        self._configuration = configuration
        pass

    @abstractmethod
    def do_request(self, **kwargs):
        """Request to server and return the response.

        Keyword args:
            kwargs: request components
        """
        pass

    @classmethod
    @abstractmethod
    def validate_request(cls, **kwargs):
        pass


