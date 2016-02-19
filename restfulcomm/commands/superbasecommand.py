"""Super base command
"""
from abc import ABCMeta, abstractmethod


class BaseCommand(metaclass=ABCMeta):

    @abstractmethod
    def execute(self):
        pass
