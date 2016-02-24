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
    def do_request(self, method, resource, headers, data):
        """Request the components to server and return the response.

        Args:
            method: str GET | POST | PUT | DELETE
            resource: str
            headers: dict
            data: dict
        """
        pass
