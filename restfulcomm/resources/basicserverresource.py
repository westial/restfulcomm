# -*- coding: utf-8 -*-
"""Server resource class for a basic action/rule definition
"""
from restfulcomm.resources.superserverresource import ServerResource


class BasicServerResource(ServerResource):

    def __init__(self, endpoint_class, api_route, route_defaults):
        """
        Construct a resource by the given endpoint_class type and route

        Args:
            endpoint_class: Endpoint class not instanced
            api_route: str
            route_defaults: dict
        """
        super().__init__(
                endpoint_class=endpoint_class,
                api_route=api_route,
                route_defaults=route_defaults
        )
        self._endpoint_class = endpoint_class
        self._api_route = api_route
        self._route_defaults = route_defaults

    @property
    def route_defaults(self):
        return self._route_defaults

    @property
    def endpoint_class(self):
        return self._endpoint_class

    @property
    def api_route(self):
        return self._api_route

