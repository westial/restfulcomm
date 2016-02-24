# -*- coding: utf-8 -*-
"""Super base command
"""
from abc import ABCMeta, abstractmethod


class BaseService(metaclass=ABCMeta):

    @abstractmethod
    def run(self, **kwargs):
        """Start service and return the result"""
        pass
