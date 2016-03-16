# -*- coding: utf-8 -*-
"""Super server resource class for an action/rule definition
"""
from abc import ABCMeta, abstractmethod, abstractproperty


class ServerResource(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, **kwargs):
        """
        Constructor

        Keyword args:
            kwargs: extensible keyword arguments
        """
        self._endpoint_class = None
        self._api_route = None

    @abstractproperty
    def endpoint_class(self):
        return self._endpoint_class

    @endpoint_class.setter
    def endpoint_class(self, value):
        """
        Args:
            value: Endpoint class definition
        """
        self._endpoint_class = value

    @abstractproperty
    def api_route(self):
        return self._api_route

    @api_route.setter
    def api_route(self, value):
        """
        Args:
            value: str
        """
        self._api_route = value
