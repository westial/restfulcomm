# -*- coding: utf-8 -*-
"""RabbitMQ client"""
import json
import time
import uuid

import pika
from restfulcomm.clients.superclient import CommClient


class RabbitMqCommClient(CommClient):
    """CommClient for RabbitMQ medium"""

    def __init__(self, configuration):
        super().__init__(configuration)

        self.response = None
        self._callback_queue = None
        self._corr_id = None
        self._pika_props = None
        self._message = None
        self._start_time = None
        self._timeout_sec = 30

        credentials = pika.PlainCredentials(
                self._configuration.value('user'),
                self._configuration.value('password')
        )

        self._connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                    host=self._configuration.value('server'),
                    virtual_host=self._configuration.value('vhost'),
                    credentials=credentials)
        )

        self._channel = self._connection.channel()

    def do_request(self, method, resource, headers, data=''):
        self._corr_id = str(uuid.uuid4())

        self._message = {
            'method': method,
            'resource': resource,
            'data': data,
            'headers': headers,
        }

        result = self._channel.queue_declare(exclusive=True)
        self._callback_queue = result.method.queue

        self._channel.basic_consume(self.on_response, no_ack=True,
                                    queue=self._callback_queue)

        self._pika_props = pika.BasicProperties(
                delivery_mode=self._configuration.value('delivery'),
                reply_to=self._callback_queue,
                correlation_id=self._corr_id,
                content_type='application/json'
        )
        return self.enqueue(message=self._message)

    def on_response(self, ch, method, properties, body):
        if self._corr_id == properties.correlation_id:
            self.response = body

    def enqueue(self, message):
        """Enqueue given dict on a rabbitmq queue server

        Args:
            message: dict
        """
        self._start_time = time.time()
        data = json.dumps(message)

        self._channel.basic_publish(
                exchange=self._configuration.value('exchange'),
                routing_key=self._configuration.value('queue'),
                properties=pika.BasicProperties(
                        reply_to=self._callback_queue,
                        correlation_id=self._corr_id,
                ),
                body=str(data)
        )

        while self.response is None \
                and time.time() - self._start_time < self._timeout_sec:
            self._connection.process_data_events()

        self._connection.close()

        return self.response
