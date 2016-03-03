# -*- coding: utf-8 -*-
"""Super for json parsers. Provides json output and a factory to create
instances of itself.
"""
import json
from abc import ABCMeta, abstractmethod


class BaseJson(metaclass=ABCMeta):

    @abstractmethod
    def __dir__(self):
        """Define the attributes able to return as json fields

        Return:
            list
        """
        pass

    def to_dict(self):
        """Return the object attributes dict"""
        attributes = dict()
        for key in self.__dir__():
            value = getattr(self, key)
            if type(value) == bytes:
                value = str(value)
            attributes[key] = value
        return attributes

    def to_json(self):
        """Return the object on json formatted plain text"""
        attributes = self.to_dict()
        return json.dumps(attributes)

    @classmethod
    @abstractmethod
    def plain_factory(cls, **kwargs):
        """Creates an instance for the given plain text content

        Keyword args:
            kwargs: mixed
        """
        pass

    @classmethod
    @abstractmethod
    def http_factory(cls, **kwargs):
        """Creates an instance for the given http object content

        Keyword args:
            kwargs: mixed
        """
        pass
