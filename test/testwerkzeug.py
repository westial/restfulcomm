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
from test.examplesettings.werkzeug import *
from test.supertestserver import SuperTestServer


class TestWerkzeug(SuperTestServer):

    def test_get(self):
        super().test_get()

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

        server_resource = BasicServerResource(
            endpoint_class,
            self.server_url_resource
        )

        server_provider = ServerProvider(
                'werkzeug',
                [server_resource],
                configuration
        )

        self._server = server_provider.server
        self._server.listen()


if __name__ == '__main__':
    unittest.main()
