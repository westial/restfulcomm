# -*- coding: utf-8 -*-
"""RabbitMQ Client Config class"""
from restfulcomm.configurations.superconfiguration import Config


class WerkzeugClientConfig(Config):

    def __init__(
            self,
            web_user,
            web_password,
            web_scheme,
            web_server,
            web_port,
            web_timeout):

        super().__init__(
            web_user,
            web_password,
            web_scheme,
            web_server,
            web_port,
            web_timeout
        )

        self._settings['user'] = web_user
        self._settings['password'] = web_password
        self._settings['scheme'] = web_scheme
        self._settings['server'] = web_server
        self._settings['port'] = web_port
        self._settings['timeout'] = web_timeout
