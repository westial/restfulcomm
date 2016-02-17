"""RabbitMQ CommServer"""
import json

import pika
from restfulcomm.servers.superserver import CommServer


class RabbitMqCommServer(CommServer):
    """CommServer for RabbitMQ server"""

    def __init__(self, command_class, configuration):
        super().__init__(command_class, configuration)

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

    def listen(self):
        self._channel.start_consuming()

    def on_request(self, ch, method, properties, body):
        """Callback function launched when client catch a job

        :param ch: object
        :param method: object
        :param properties: (not used here)
        :param body: str
        :return: void
        """
        resource = self._command_class(raw_content=body)
        raw_response = resource.execute()

        if raw_response:
            response = json.dumps(raw_response)
            ch.basic_publish(exchange=self._configuration.value('exchange'),
                             routing_key=properties.reply_to,
                             properties=pika.BasicProperties(
                                     correlation_id=properties.correlation_id
                             ),
                             body=response)

        ch.basic_ack(delivery_tag=method.delivery_tag)

        return
