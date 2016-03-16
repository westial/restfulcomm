# -*- coding: utf-8 -*-
"""RabbitMQ Client Config class"""
from restfulcomm.configurations.superconfiguration import Config


class RabbitMqClientConfig(Config):

    def __init__(
            self,
            rmq_user,
            rmq_password,
            rmq_server,
            rmq_vhost,
            rmq_queue,
            rmq_delivery,
            rmq_exchange,
            rmq_timeout):

        super().__init__(
            rmq_user,
            rmq_password,
            rmq_server,
            rmq_vhost,
            rmq_queue,
            rmq_delivery,
            rmq_exchange,
            rmq_timeout
        )

        self._settings['user'] = rmq_user
        self._settings['password'] = rmq_password
        self._settings['server'] = rmq_server
        self._settings['vhost'] = rmq_vhost
        self._settings['queue'] = rmq_queue
        self._settings['delivery'] = rmq_delivery
        self._settings['exchange'] = rmq_exchange
        self._settings['timeout'] = rmq_timeout
