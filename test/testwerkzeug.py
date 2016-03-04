#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test cases for werkzeug server"""
import unittest
from _thread import start_new_thread

import time

from restfulcomm.configurations.werkzeugclientconfig import WerkzeugClientConfig
from restfulcomm.configurations.werkzeugserverconfig import WerkzeugServerConfig
from restfulcomm.providers.clientprovider import ClientProvider
from restfulcomm.providers.serverprovider import ServerProvider
from restfulcomm.resources.basicserverresource import BasicServerResource
from test.examplelib.successendpoint import SuccessEndpoint
from test.examplesettings.werkzeug import *


class TestWerkzeug(unittest.TestCase):

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

        except Exception as e:
            print(e)

        finally:
            self.reset_server()

    @classmethod
    def build_client_provider(cls):
        configuration = WerkzeugClientConfig(
                web_user=None,
                web_password=None,
                web_scheme=WEB_SCHEME,
                web_server=WEB_HOST,
                web_port=WEB_PORT,
                web_timeout=WEB_TIMEOUT
        )

        provider = ClientProvider('werkzeug', configuration)

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
        configuration = WerkzeugServerConfig(
            web_user=None,
            web_password=None,
            web_server=WEB_HOST,
            web_port=WEB_PORT,
            use_debugger=USE_DEBUGGER,
            use_reloader=USE_RELOADER
        )

        server_resource = BasicServerResource(endpoint_class, '/index/<content>')

        server_provider = ServerProvider(
                'werkzeug',
                [server_resource],
                configuration
        )

        self._server = server_provider.server
        self._server.listen()

    # def test_start_server(self):
    #     configuration = WerkzeugServerConfig(
    #         web_user=None,
    #         web_password=None,
    #         web_server=WEB_HOST,
    #         web_port=WEB_PORT,
    #         use_debugger=USE_DEBUGGER,
    #         use_reloader=USE_RELOADER
    #     )
    #
    #     server_resource = BasicServerResource(SuccessEndpoint, '/index/<content>')
    #
    #     server_provider = ServerProvider(
    #             'werkzeug',
    #             [server_resource],
    #             configuration
    #     )
    #
    #     self._server = server_provider.server
    #     self._server.listen()


if __name__ == '__main__':
    unittest.main()
