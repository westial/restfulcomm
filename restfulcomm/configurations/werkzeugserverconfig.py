# -*- coding: utf-8 -*-
"""Werkzeug Server Config class"""
from restfulcomm.configurations.superconfiguration import Config


class WerkzeugServerConfig(Config):

    def __init__(
            self,
            web_user,
            web_password,
            web_server,
            web_port,
            use_debugger,
            use_reloader):

        super().__init__(
            web_user,
            web_password,
            web_server,
            web_port,
            use_debugger,
            use_reloader
        )

        self._settings['user'] = web_user
        self._settings['password'] = web_password
        self._settings['server'] = web_server
        self._settings['port'] = web_port
        self._settings['use_debugger'] = use_debugger
        self._settings['use_reloader'] = use_reloader
