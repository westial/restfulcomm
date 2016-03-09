#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test cases for all supported servers"""


import unittest
from _thread import start_new_thread
from abc import ABCMeta, abstractmethod

import time

from restfulcomm.resources.basicserverresource import BasicServerResource
from test.examplelib.imageendpoint import ImageEndpoint
from test.examplelib.successendpoint import SuccessEndpoint


class SuperTestServer(unittest.TestCase, metaclass=ABCMeta):

    __server = None

    @classmethod
    def _server(cls):
        if cls.__server:
            return cls.__server
        else:
            raise ValueError('Server is still not set')

    @classmethod
    def set_server(cls, server):
        if not cls.__server:
            cls.__server = server

    def setUp(self):
        self._server = None
        self.message_for_get = 'This is my print response example message'
        self.resource_pattern_for_get = '/index/{!s}'
        self.headers_for_get = {'a': 'first', 'b': 'second'}

    @classmethod
    def setUpClass(cls):
        endpoints_context = [
            (SuccessEndpoint, '/index/<content>'),
            (ImageEndpoint, '/python.jpg'),
        ]
        cls.start_server(endpoints_context)

    @classmethod
    def tearDownClass(cls):
        cls.reset_server()

    def test_get(self):
        """Client requests a simple message and server returns the message as
         response"""
        message = self.message_for_get
        self.headers_for_get.update({'Content-type': 'text/plain'})

        client_provider = self.build_client_provider()

        json_response = client_provider.client.do_request(
                method='GET',
                resource=self.resource_pattern_for_get.format(message),
                headers=self.headers_for_get
        )

        self.assertEqual(json_response.status, 200)
        self.assertEqual(json_response.body, message)

    def test_get_not_found(self):
        """Client requests a route and server returns a not found status code"""
        self.headers_for_get.update({'Content-type': 'text/plain'})

        client_provider = self.build_client_provider()

        json_response = client_provider.client.do_request(
                method='GET',
                resource='/path/to/missing/page',
                headers=self.headers_for_get
        )

        self.assertEqual(json_response.status, 404)

    def test_get_image(self):
        """Client requests the properly route and server returns a binary image
        file"""
        img_path = ImageEndpoint.publish_img_path()
        self.headers_for_get.update({'Content-type': 'image/png'})

        with open(img_path, 'rb') as img_file:
            img_content = img_file.read()

        client_provider = self.build_client_provider()

        json_response = client_provider.client.do_request(
                method='GET',
                resource='/python.jpg',
                headers=self.headers_for_get
        )

        self.assertEqual(json_response.status, 200)
        self.assertEqual(json_response.body[:50], img_content[:50])

    @classmethod
    @abstractmethod
    def build_client_provider(cls):
        """Create and return a ClientProvider
        """
        pass

    @abstractmethod
    def _async_server(self, endpoints_context):
        """Asynchronous server listening

        Args:
            endpoints_context: tuple<Endpoint class, resource str>
        """
        pass

    @classmethod
    def start_server(cls, endpoints_context):
        start_new_thread(cls._async_server, (endpoints_context,))
        time.sleep(5)

    @classmethod
    def reset_server(cls):
        cls._server().reset()

    @classmethod
    def endpoints_to_server_resources(cls, endpoints_context):
        server_resources = list()

        while len(endpoints_context):
            endpoint_context = endpoints_context.pop()

            server_resource = BasicServerResource(
                endpoint_context[0],
                endpoint_context[1]
            )

            server_resources.append(server_resource)

        return server_resources
