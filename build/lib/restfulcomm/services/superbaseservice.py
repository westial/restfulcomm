# -*- coding: utf-8 -*-
"""Super base command
"""
from abc import ABCMeta, abstractmethod


class BaseService(metaclass=ABCMeta):

    @classmethod
    @abstractmethod
    def run(cls, **kwargs):
        """Start service and return the result"""
        pass
