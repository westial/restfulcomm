# -*- coding: utf-8 -*-
"""A simple URL simple server using Werkzeug providing configuration and rules
setting up by the constructor parameters.
"""

from restfulcomm.servers.superserver import CommServer
from werkzeug.wrappers import Request
from werkzeug.routing import Map, Rule
from werkzeug.serving import run_simple


class WerkzeugCommServer(CommServer):

    def __init__(self, server_resources, configuration):
        super().__init__(server_resources, configuration)

        self._url_map = Map()
        self._endpoints = dict()

        self._create_rules()

        self._environ = None

    def _dispatch_request(self, request):
        """Dispatches request and returns the response

        Args:
            request: Request object

        Return:
            JsonResponse
        """
        router = self._url_map.bind_to_environ(request.environ)
        endpoint_name, values = router.match()
        endpoint = self._endpoints[endpoint_name]

        json_response = getattr(
                endpoint,
                request.method
        )(request.form, **values)

        return json_response

    def listen(self):
        run_simple(
                self._configuration.value('server'),
                self._configuration.value('port'),
                self,
                use_debugger=self._configuration.value('use_debugger'),
                use_reloader=self._configuration.value('use_reloader')
        )

    def stop(self):
        if 'werkzeug.server.shutdown' not in self._environ:
            raise RuntimeError('Not running the development server')
        self._environ['werkzeug.server.shutdown']()

    def _create_rules(self):
        while self._resources:
            resource = self._resources.pop(0)
            endpoint_name = resource.endpoint_class.__name__
            self._endpoints[endpoint_name] = resource.endpoint_class
            self._url_map.add(
                    Rule(resource.api_route, endpoint=endpoint_name)
            )

    def wsgi_app(self, environ, start_response):
        request = Request(environ)
        response = self._dispatch_request(request=request)
        return response(environ, start_response)

    def __call__(self, environ, start_response):
        return self.wsgi_app(environ, start_response)
