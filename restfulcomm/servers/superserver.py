# -*- coding: utf-8 -*-
"""Super server class"""
from abc import ABCMeta, abstractmethod


class CommServer(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, server_resources, configuration):
        """Configures the resource for exit

        Args:
            server_resources: list ServerResource classes definition

        Keyword args:
            configuration: Config server configuration object
        """
        self._resources = server_resources
        self._configuration = configuration

    @abstractmethod
    def _create_rules(self):
        """Creates and configures the rules for the server resources given
        on instance construction"""
        pass

    @abstractmethod
    def _dispatch_request(self, **kwargs):
        """Runs the command action by the given resource endpoint"""
        pass

    @abstractmethod
    def listen(self):
        """Request the given content to server and return the response"""
        pass

    @abstractmethod
    def stop(self):
        """Shutdown server"""
        pass

    @abstractmethod
    def reset(self):
        """Clean and shutdown server"""
        pass
