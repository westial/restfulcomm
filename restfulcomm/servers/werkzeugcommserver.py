# -*- coding: utf-8 -*-
"""A simple URL simple server using Werkzeug providing configuration and rules
setting up by the constructor parameters.
"""

from restfulcomm.servers.superserver import CommServer
from werkzeug.exceptions import NotFound
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
            HTTP Response
        """
        router = self._url_map.bind_to_environ(request.environ)

        try:
            endpoint_name, values = router.match()

        except NotFound:
            return self.not_found()

        endpoint = self._endpoints[endpoint_name]

        http_response = getattr(
                endpoint,
                request.method
        )(request.form, **values)

        return http_response

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

    def reset(self):
        self.stop()

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
        self._environ = environ
        return self.wsgi_app(environ, start_response)
