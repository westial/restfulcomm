#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test cases for werkzeug server"""
import unittest

from restfulcomm.configurations.werkzeugclientconfig import WerkzeugClientConfig
from restfulcomm.configurations.werkzeugserverconfig import WerkzeugServerConfig
from restfulcomm.providers.clientprovider import ClientProvider
from restfulcomm.providers.serverprovider import ServerProvider
from test.examplesettings.werkzeug import *
from test.supertestserver import SuperTestServer


class TestWerkzeug(SuperTestServer):

    def test_delete(self):
        super().test_delete()

    def test_post(self):
        super().test_post()

    def test_post_json(self):
        super().test_post_json()

    def test_put(self):
        super().test_put()

    def test_get_not_found(self):
        super().test_get_not_found()

    def test_get(self):
        super().test_get()

    def test_get_params(self):
        super().test_get_params()

    def test_get_image(self):
        super().test_get_image()

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

    @classmethod
    def _async_server(cls, endpoints_context):
        configuration = WerkzeugServerConfig(
            web_user=None,
            web_password=None,
            web_server=WEB_HOST,
            web_port=WEB_PORT,
            use_debugger=USE_DEBUGGER,
            use_reloader=USE_RELOADER
        )

        server_resources = cls.endpoints_to_server_resources(endpoints_context)

        server_provider = ServerProvider(
                'werkzeug',
                server_resources,
                configuration
        )

        cls.set_server(server_provider.server)
        cls._server().listen()


if __name__ == '__main__':
    unittest.main()
