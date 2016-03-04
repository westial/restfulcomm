# -*- coding: utf-8 -*-
"""Werkzeug client"""
from requests.auth import HTTPBasicAuth

from restfulcomm.clients.superclient import CommClient
from restfulcomm.http.jsonresponse import JsonResponse
from restfulcomm.services.httprequestservice import HttpRequestService


class WerkzeugCommClient(CommClient):
    """CommClient for Werkzeug medium"""

    def __init__(self, configuration):
        super().__init__(configuration)

        self.response = None
        self._message = None
        self._start_time = None
        self._timeout_sec = 30

        self._credentials = HTTPBasicAuth(
                self._configuration.value('user'),
                self._configuration.value('password')
        )

    def do_request(self, method, resource, headers, data=None, params=None):

        http_response = HttpRequestService.run(
            method=method,
            scheme=self._configuration.value('scheme'),
            domain=self._configuration.value('server'),
            port=self._configuration.value('port'),
            resource=resource,
            headers=headers,
            data=data,
            params=params,
            timeout=self._configuration.value('timeout')
        )

        return JsonResponse.http_factory(http_response)

