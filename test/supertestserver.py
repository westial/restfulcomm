#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test cases for all supported servers"""


import unittest
from _thread import start_new_thread
from abc import ABCMeta, abstractmethod

import time

from test.examplelib.successendpoint import SuccessEndpoint


class SuperTestServer(unittest.TestCase, metaclass=ABCMeta):

    def setUp(self):
        self._server = None
        self.message_for_get = 'This is my print response example message'
        self.resource_pattern_for_get = '/index/{!s}'
        self.headers_for_get = {'a': 'first', 'b': 'second'}
        self.server_url_resource = '/index/<content>'

    def test_get(self):

        try:
            message = self.message_for_get

            self.start_server(SuccessEndpoint)

            client_provider = self.build_client_provider()

            json_response = client_provider.client.do_request(
                    method='GET',
                    resource=self.resource_pattern_for_get.format(message),
                    headers=self.headers_for_get
            )

            self.assertEqual(json_response.status, 200)
            self.assertEqual(json_response.body, message)

        finally:
            self.reset_server()

    @classmethod
    @abstractmethod
    def build_client_provider(cls):
        """Create and return a ClientProvider
        """
        pass

    @abstractmethod
    def _async_server(self, endpoint_class):
        """Asynchronous server listening

        Args:
            endpoint_class: Endpoint class
        """
        pass

    def start_server(self, endpoint_class):
        start_new_thread(self._async_server, (endpoint_class, ))
        time.sleep(5)

    def reset_server(self):
        self._server.reset()