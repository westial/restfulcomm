# -*- coding: utf-8 -*-
"""Value object product of a json format request got from a client as plain
text.
"""
import json

from restfulcomm.http.superjson import BaseJson
from requests.models import Request
from urllib.parse import urlparse


class JsonRequest(BaseJson):

    def __init__(self):
        super().__init__()
        self.scheme = None
        self.host = None
        self.port = None
        self.method = None
        self.resource = None
        self.data = None
        self.params = None
        self.headers = None
        self.files = None

    def __dir__(self):
        return [
            'scheme',
            'host',
            'port',
            'method',
            'resource',
            'data',
            'params',
            'headers',
            'files'
        ]

    def get_http(self):
        """Return an HTTP Request formatted attributes"""
        request = Request(
            method=self.method,
            url='{scheme}{host}:{port}{resource}'.format(
                scheme=self.scheme,
                host=self.host,
                port=self.port,
                resource=self.resource
            ),
            params=self.params,
            files=self.files)

        return request

    @classmethod
    def plain_factory(cls, content):
        """Given a plain text json formatted content sets the attributes

        Args:
            content: str json formatted content

        Return:
            JsonRequest object
        """
        if type(content) == bytes:
            content = content.decode('utf-8')

        json_map = json.loads(content)

        json_request = JsonRequest()

        json_request.method = json_map['method']

        if 'resource' in json_map:
            json_request.resource = json_map['resource']

        if 'headers' in json_map:
            json_request.headers = json_map['headers']

        if 'params' in json_map:
            json_request.params = json_map['params']

        if 'data' in json_map:
            json_request.data = json_map['data']

        if 'files' in json_map:
            json_request.files = json_map['files']

        return json_request

    @classmethod
    def decompose_url(cls, url, json_request):
        parsed_url = urlparse(url)

        json_request.scheme = parsed_url.scheme
        json_request.port = parsed_url.port
        json_request.host = parsed_url.hostname
        json_request.resource = parsed_url.path

        return json_request

    @classmethod
    def http_factory(cls, request: Request):
        json_request = JsonRequest()

        json_request = cls.decompose_url(request.url, json_request)
        json_request.method = request.method
        json_request.data = request.data
        json_request.params = request.params

        if request.headers:
            json_request.headers = dict(request.headers)

        if request.files:
            json_request.files = list(request.files)

    @classmethod
    def build_params(cls, immutable_dict):
        """
        :param immutable_dict:
        :return: dict|None
        """
        if not immutable_dict:
            return None
        items = dict()
        for param in immutable_dict:
            items.update({param: immutable_dict[param]})
        return items
