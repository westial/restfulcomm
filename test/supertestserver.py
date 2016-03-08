#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test cases for all supported servers"""


import unittest
from _thread import start_new_thread
from abc import ABCMeta, abstractmethod

import time

from test.examplelib.imageendpoint import ImageEndpoint
from test.examplelib.successendpoint import SuccessEndpoint
from test.examplesettings.globals import TEST_ROOT_PATH


class SuperTestServer(unittest.TestCase, metaclass=ABCMeta):

    def setUp(self):
        self._server = None
        self.message_for_get = 'This is my print response example message'
        self.resource_pattern_for_get = '/index/{!s}'
        self.headers_for_get = {'a': 'first', 'b': 'second'}

    def test_get(self):
        """Client requests a simple message and server returns the message as
         response"""

        try:
            message = self.message_for_get
            self.headers_for_get.update({'Content-type': 'text/plain'})

            self.start_server(SuccessEndpoint, '/index/<content>')

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

    def test_get_image(self):
        """Client requests the properly route and server returns a binary image
        file"""

        try:
            img_path = ImageEndpoint.publish_img_path()
            self.headers_for_get.update({'Content-type': 'image/png'})

            with open(img_path, 'rb') as img_file:
                img_content = img_file.read()

            self.start_server(ImageEndpoint, '/python.jpg')

            client_provider = self.build_client_provider()

            json_response = client_provider.client.do_request(
                    method='GET',
                    resource='/python.jpg',
                    headers=self.headers_for_get
            )

            self.assertEqual(json_response.status, 200)
            self.assertEqual(json_response.body[:50], img_content[:50])

        finally:
            self.reset_server()

    @classmethod
    @abstractmethod
    def build_client_provider(cls):
        """Create and return a ClientProvider
        """
        pass

    @abstractmethod
    def _async_server(self, endpoint_class, resource):
        """Asynchronous server listening

        Args:
            endpoint_class: Endpoint class
            resource: url query resources
        """
        pass

    def start_server(self, endpoint_class, resource):
        start_new_thread(self._async_server, (endpoint_class, resource,))
        time.sleep(5)

    def reset_server(self):
        self._server.reset()
