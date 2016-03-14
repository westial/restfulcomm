# -*- coding: utf-8 -*-
"""Value object product of a json format response got from a server as plain
text.
"""
import base64
import json

from restfulcomm.http.superjson import BaseJson
from restfulcomm.core.helpers import HttpHelper
from requests.models import Response


class JsonResponse(BaseJson):

    def to_dict(self):
        """Return the object attributes dict. If content type is not plain text
        encode the body by base64 codec"""
        attributes = dict()
        for key in self.__dir__():
            value = getattr(self, key)
            if key == 'body' and not HttpHelper.is_plain_content_type(
                    self.headers['Content-Type']):
                value = base64.b64encode(value).decode()
            attributes[key] = value
        return attributes

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
    def plain_factory(cls, content):
        """Given a plain text json formatted content sets the context attributes

        Args:
            content: str json formatted content

        Return:
            JsonResponse object
        """
        if type(content) == bytes:
            content = content.decode('utf-8')

        json_map = json.loads(content)

        json_response = JsonResponse()

        json_response.headers = json_map['headers']
        json_response.status = json_map['status']

        if 'body' in json_map:
            if HttpHelper.is_plain_content_type(json_response.headers['Content-Type']):
                json_response.body = json_map['body']
            else:
                json_response.body = base64.b64decode(json_map['body'])
        else:
            json_response.body = None

        return json_response

    @classmethod
    def http_factory(cls, response: Response):
        """Return a JsonResponse object by the given HTTP Response

        Args:
            response: Response object

        Return:
            JsonResponse
        """
        json_response = JsonResponse()

        if response.encoding:
            json_response.body = response.content.decode(response.encoding)
        else:
            json_response.body = response.content

        json_response.status = response.status_code
        json_response.headers = dict(response.headers)

        return json_response

