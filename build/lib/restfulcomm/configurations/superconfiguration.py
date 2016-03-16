# -*- coding: utf-8 -*-
"""Super class for server/client configuration"""
from abc import ABCMeta, abstractmethod


class Config(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, *settings):
        """Initialize the configuration object by the given settings.
        The settings are stored into a dict"""
        self._settings = dict()
        pass

    def value(self, key):
        """Return the value for the given key from the settings dict.

        Args:
             key: int|str
        """
        return self._settings[key]
