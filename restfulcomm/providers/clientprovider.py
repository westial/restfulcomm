# -*- coding: utf-8 -*-
"""Entry point for client resources"""
from restfulcomm.clients.rabbitmqclient import RabbitMqCommClient
from restfulcomm.clients.werkzeugclient import WerkzeugCommClient


class ClientProvider(object):
    """Client provider"""

    def __init__(self, client_type, configuration):
        """Configure a client by the given type

        Args:
            client_type: str. By the moment only rabbitmq value is allowed.
            configuration: Config client configuration object

        Raises:
            TypeError if client_type is an unexpected value.
        """
        if client_type == 'rabbitmq':
            client_class = RabbitMqCommClient
        elif client_type == 'werkzeug':
            client_class = WerkzeugCommClient
        else:
            raise TypeError('Unexpected client type')

        self._client = self.factory(client_class, configuration)

    @property
    def client(self):
        return self._client

    @classmethod
    def factory(cls, client_class, configuration):
        return client_class(configuration)
