# -*- coding: utf-8 -*-
"""Given a werkzeug http response provide json formatted response result"""
import re

from restfulcomm.core.helpers import HttpHelper
from restfulcomm.services.superbaseservice import BaseService
from restfulcomm.http.jsonresponse import JsonResponse
from werkzeug.wrappers import Response


class HttpResponseToJsonService(BaseService):

    @classmethod
    def run(cls, response):
        """
        :param response: HTTP Response
        :return: JsonResponse
        """
        json_response = cls.factory(response)
        return json_response

    @classmethod
    def extract_charset(cls, content_type):
        """Extract and return the charset from the content type header value.
        Response charset is always set as default, also if the content type
        header is not containing its value.

        :param content_type: str
        :return str|None
        """
        match = re.search(
            '.*charset=([^ ;]*)',
            content_type,
            re.IGNORECASE
        )

        if match:
            return match.group(1)

        return None

    @classmethod
    def factory(cls, response: Response):
        """Return a JsonResponse object by the given Response

        Args:
            response: HTTP Response

        Return:
            JsonResponse
        """
        json_response = JsonResponse()

        charset = cls.extract_charset(response.content_type)

        if charset:
            json_response.body = response.data.decode(charset)

        elif HttpHelper.is_plain_content_type(response.content_type):
            json_response.body = response.data.decode(response.charset)

        else:
            json_response.body = response.data

        json_response.status = response.status_code
        json_response.headers = dict(response.headers)

        return json_response
