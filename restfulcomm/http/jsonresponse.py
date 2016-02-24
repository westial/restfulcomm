# -*- coding: utf-8 -*-
"""Value object product of a json format response got from a server as plain
text.
"""
import json

from restfulcomm.http.superjson import BaseJson


class JsonResponse(BaseJson):

    def __init__(self):
        self._status = None
        self._body = None
        self._headers = None

    def __dir__(self):
        return [
            'status',
            'body',
            'headers'
        ]

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    @property
    def body(self):
        return self._body

    @body.setter
    def body(self, value):
        self._body = value

    @property
    def headers(self):
        return self._headers

    @headers.setter
    def headers(self, value):
        self._headers = value

    @classmethod
    def factory(cls, content):
        """Given a plain text json formatted content sets the attributes

        Args:
            content: str json formatted content

        Return:
            JsonResponse object
        """
        if type(content) == bytes:
            content = content.decode('utf-8')

        json_map = json.loads(content)

        json_response = JsonResponse()

        json_response.status = json_map['status']

        if 'body' in json_map:
            json_response.body = json_map['body']
        else:
            json_response.body = None

        if 'headers' in json_map:
            json_response.headers = json_map['headers']
        else:
            json_response.headers = None

        return json_response
