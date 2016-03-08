#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test cases for rabbitmq server"""
import unittest
from restfulcomm.configurations.rabbitmqclientconfig import RabbitMqClientConfig
from restfulcomm.configurations.rabbitmqserverconfig import RabbitMqServerConfig
from restfulcomm.providers.clientprovider import ClientProvider
from restfulcomm.providers.serverprovider import ServerProvider
from restfulcomm.resources.basicserverresource import BasicServerResource
from test.examplesettings.rabbitmq import *
from test.supertestserver import SuperTestServer


class TestRabbitMq(SuperTestServer):

    def test_get(self):
        super().test_get()

    def test_get_image(self):
        super().test_get_image()

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

    @classmethod
    def _async_server(cls, endpoints_context):
        configuration = RabbitMqServerConfig(
                rmq_user=RABBITMQ_USER,
                rmq_password=RABBITMQ_PASSWORD,
                rmq_server=RABBITMQ_SERVER,
                rmq_vhost=RABBITMQ_VHOST,
                rmq_queue=RABBITMQ_QUEUE,
                rmq_prefetch=RABBITMQ_PREFETCH_COUNT,
                rmq_exchange=RABBITMQ_EXCHANGE
        )

        server_resources = cls.endpoints_to_server_resources(endpoints_context)

        server_provider = ServerProvider(
                'rabbitmq',
                server_resources,
                configuration
        )

        cls.set_server(server_provider.server)
        cls._server().listen()


if __name__ == '__main__':
    unittest.main()
