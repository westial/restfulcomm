# -*- coding: utf-8 -*-
"""RabbitMQ CommServer"""

import pika
from restfulcomm.http.jsonrequest import JsonRequest
from restfulcomm.servers.superserver import CommServer
from restfulcomm.services.httpresponsetojsonservice import \
    HttpResponseToJsonService
from werkzeug.exceptions import NotFound
from werkzeug.routing import Map, Rule
from werkzeug.wrappers import Response


class RabbitMqCommServer(CommServer):
    """CommServer for RabbitMQ server"""

    def __init__(self, server_resources, configuration):
        super().__init__(server_resources, configuration)

        self._url_map = Map()
        self._endpoints = dict()

        self._create_rules()

        credentials = pika.PlainCredentials(
                self._configuration.value('user'),
                self._configuration.value('password')
        )

        self._connection = pika.BlockingConnection(
                pika.ConnectionParameters(
                        host=self._configuration.value('server'),
                        virtual_host=self._configuration.value('vhost'),
                        credentials=credentials
                )
        )
        self._channel = self._connection.channel()
        self._channel.queue_declare(queue=self._configuration.value('queue'))
        self._channel.basic_qos(
                prefetch_count=self._configuration.value('prefetch')
        )
        self._channel.basic_consume(
                self.on_request,
                queue=self._configuration.value('queue')
        )

    def _dispatch_request(self, body):
        """Dispatches request and returns the response

        Args:
            body: str

        Return:
            HTTP Response
        """
        json_request = JsonRequest.plain_factory(content=body)
        router = self._url_map.bind(
                server_name='',
                path_info=json_request.resource
        )

        try:
            endpoint_name, values = router.match()

        except NotFound:
            return Response('Not Found', status=404)

        endpoint = self._endpoints[endpoint_name]

        http_response = getattr(
                endpoint,
                json_request.method
        )(json_request.data, **values)

        return http_response

    def _create_rules(self):
        while self._resources:
            resource = self._resources.pop(0)
            endpoint_name = resource.endpoint_class.__name__
            self._endpoints[endpoint_name] = resource.endpoint_class
            self._url_map.add(
                    Rule(resource.api_route, endpoint=endpoint_name)
            )

    def listen(self):
        self._channel.start_consuming()

    def stop(self):
        self._channel.cancel()

    def purge(self):
        self._channel.queue_purge(self._configuration.value('queue'))

    def reset(self):
        self._channel.queue_purge(self._configuration.value('queue'))
        self._channel.cancel()
        self._channel.queue_delete(self._configuration.value('queue'))

    def on_request(self, ch, method, properties, body):
        """Callback function launched when client catch a job

        Args:
            ch: object
            method: object
            properties: (not used here)
            body: str
        """
        http_response = self._dispatch_request(body)

        json_response = HttpResponseToJsonService.run(response=http_response)

        if json_response:
            ch.basic_publish(exchange=self._configuration.value('exchange'),
                             routing_key=properties.reply_to,
                             properties=pika.BasicProperties(
                                     correlation_id=properties.correlation_id
                             ),
                             body=json_response.to_json())

        ch.basic_ack(delivery_tag=method.delivery_tag)

        return
