# -*- coding: utf-8 -*-
"""HTTP Requests service"""
import json

import requests
from restfulcomm.services.superbaseservice import BaseService


class HttpRequestService(BaseService):
    """Http Requester"""

    @classmethod
    def run(cls,
            method,
            scheme,
            domain,
            port,
            resource,
            headers=None,
            data=None,
            params=None,
            timeout=None,
            auth=None
            ):
        """
        Request to the given url with the given configuration and return the
        response.

        :param method: str. Allowed values: POST|PUT|GET|DELETE
        :param scheme: str
        :param domain: str
        :param port: int
        :param resource: str, starting from root with slash
        :param headers: None|dict
        :param data: None|dict
        :param params: None|dict
        :param timeout: None|int
        :param auth: None|HTTPBasicAuth object
        :return: Response object
        """
        route = '{!s}://{!s}:{:d}{!s}'.format(
            scheme,
            domain,
            port,
            resource
        )

        data = cls._encapsulate_json(headers['Content-Type'], data=data)

        if method.upper() == 'POST':
            response = cls._request_post(
                route,
                data,
                params,
                timeout,
                headers,
                auth)

        elif method.upper() == 'PUT':
            response = cls._request_put(
                route,
                data,
                params,
                timeout,
                headers,
                auth)

        elif method.upper() == 'GET':
            response = cls._request_get(
                route,
                params,
                timeout,
                headers,
                auth)

        elif method.upper() == 'DELETE':
            response = cls._request_delete(
                route,
                params,
                timeout,
                headers,
                auth)

        else:
            raise ValueError('Unexpected method {!s}'.format(method))

        return response

    @classmethod
    def _encapsulate_json(cls, content_type, data):
        """Converts a content type json formatted data to an encapsulated
        content supported by the http server response parser.
        :param content_type: str
        :param data: mixed
        :return mixed
        """
        if data and content_type == 'application/json':
            data = json.dumps({'json_data': data})
        return data

    @classmethod
    def _request_post(cls, route, data, params, timeout, headers, auth):
        """
        Makes a post request.
        :param route: str
        :param data: dict
        :param params: dict
        :param timeout: int
        :param headers: dict
        :param auth: object
        :return: Http Response
        """
        response = requests.post(
            route,
            data=data,
            params=params,
            timeout=timeout,
            headers=headers,
            auth=auth)
        return response

    @classmethod
    def _request_put(cls, route, data, params, timeout, headers, auth):
        """
        Makes a put request.
        :param route: str
        :param data: dict
        :param params: dict
        :param timeout: int
        :param headers: dict
        :param auth: object
        :return: Http Response
        """
        response = requests.put(
            route,
            data=data,
            params=params,
            timeout=timeout,
            headers=headers,
            auth=auth)
        return response

    @classmethod
    def _request_get(cls, route, params, timeout, headers, auth):
        """
        Makes a get request.
        :param route: str
        :param params: dict
        :param timeout: int
        :param headers: dict
        :param auth: object
        :return: Http Response
        """
        response = requests.get(
            route,
            params=params,
            timeout=timeout,
            headers=headers,
            auth=auth)
        return response

    @classmethod
    def _request_delete(cls, route, params, timeout, headers, auth):
        """
        Makes a delete request.
        :param route: str
        :param params: dict
        :param timeout: int
        :param headers: dict
        :param auth: object
        :return: Http Response
        """
        response = requests.delete(
            route,
            params=params,
            timeout=timeout,
            headers=headers,
            auth=auth
        )
        return response
