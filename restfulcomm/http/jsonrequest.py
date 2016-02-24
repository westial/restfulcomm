# -*- coding: utf-8 -*-
"""Value object product of a json format request got from a client as plain
text.
"""
import json

from restfulcomm.http.superjson import BaseJson


class JsonRequest(BaseJson):

    def __init__(self):
        self.scheme = None
        self.host = None
        self.port = None
        self.method = None
        self.resource = None
        self.data = None
        self.headers = None

    def __dir__(self):
        return [
            'method',
            'resource',
            'headers',
            'data'
        ]

    @classmethod
    def factory(cls, content):
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
        json_request.resource = json_map['resource']

        if 'headers' in json_map:
            json_request.headers = json_map['headers']

        if 'data' in json_map:
            json_request.data = json_map['data']

        return json_request
