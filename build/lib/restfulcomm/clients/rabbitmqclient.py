# -*- coding: utf-8 -*-
"""RabbitMQ client"""
import json
import time
import uuid

import pika
from restfulcomm.clients.superclient import CommClient
from restfulcomm.http.jsonresponse import JsonResponse


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
        self._channel = None
        self._timeout_sec = self._configuration.value('timeout')

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

    @classmethod
    def validate_request(cls, headers):
        if 'Content-type' not in headers:
            raise ValueError('Content type header is mandatory')

    def do_request(self, method, resource, headers, data=None, params=None):
        self.validate_request(headers=headers)

        self._corr_id = str(uuid.uuid4())

        self._message = {
            'method': method,
            'resource': resource,
            'data': data,
            'params': params,
            'headers': headers,
        }

        self._channel = self._connection.channel()

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
        plain_json_response = self.enqueue(message=self._message)

        json_response = JsonResponse.plain_factory(plain_json_response)

        return json_response

    def _clean_response(self):
        """Clean response attribute preparing for next operations"""
        self.response = None

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
                body=data
        )

        while self.response is None \
                and time.time() - self._start_time < self._timeout_sec:
            self._connection.process_data_events()

        response = self.response
        self._clean_response()

        return response
