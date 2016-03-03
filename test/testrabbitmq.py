#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test cases for rabbitmq server"""
import unittest
from _thread import start_new_thread

import time

from restfulcomm.configurations.rabbitmqclientconfig import RabbitMqClientConfig
from restfulcomm.configurations.rabbitmqserverconfig import RabbitMqServerConfig
from restfulcomm.providers.clientprovider import ClientProvider
from restfulcomm.providers.serverprovider import ServerProvider
from restfulcomm.resources.basicserverresource import BasicServerResource
from test.examplelib.successendpoint import SuccessEndpoint
from test.examplesettings.rabbitmq import *


class TestRabbitMq(unittest.TestCase):

    def setUp(self):
        self._server = None

    def test_get(self):

        try:
            message = 'This is my print response example message'

            self.start_server(SuccessEndpoint)

            client_provider = self.build_client_provider()

            json_response = client_provider.client.do_request(
                    method='GET',
                    resource='/index/{!s}'.format(message),
                    headers={'a': 'first', 'b': 'second'}
            )

            self.assertEqual(json_response.status, 200)
            self.assertEqual(json_response.body, message)

        finally:
            self.reset_server()

    @classmethod
    def build_client_provider(cls):
        configuration = RabbitMqClientConfig(
                rmq_user=RABBITMQ_USER,
                rmq_password=RABBITMQ_PASSWORD,
                rmq_server=RABBITMQ_SERVER,
                rmq_vhost=RABBITMQ_VHOST,
                rmq_queue=RABBITMQ_QUEUE,
                rmq_delivery=RABBITMQ_DELIVERY_MODE,
                rmq_exchange=RABBITMQ_EXCHANGE,
                rmq_timeout=RABBITMQ_TIMEOUT,
        )

        provider = ClientProvider('rabbitmq', configuration)

        return provider

    def start_server(self, endpoint_class):
        start_new_thread(self._async_server, (endpoint_class, ))
        time.sleep(5)

    def reset_server(self):
        self._server.reset()

    def _async_server(self, endpoint_class):
        """Asynchronous server listening

        Args:
            endpoint_class: Endpoint class
        """
        configuration = RabbitMqServerConfig(
                rmq_user=RABBITMQ_USER,
                rmq_password=RABBITMQ_PASSWORD,
                rmq_server=RABBITMQ_SERVER,
                rmq_vhost=RABBITMQ_VHOST,
                rmq_queue=RABBITMQ_QUEUE,
                rmq_prefetch=RABBITMQ_PREFETCH_COUNT,
                rmq_exchange=RABBITMQ_EXCHANGE
        )

        server_resource = BasicServerResource(endpoint_class, '/index/<content>')

        server_provider = ServerProvider(
                'rabbitmq',
                [server_resource],
                configuration
        )

        self._server = server_provider.server
        self._server.listen()


if __name__ == '__main__':
    unittest.main()
