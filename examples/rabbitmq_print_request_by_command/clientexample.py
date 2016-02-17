"""Client example sending messages by any method"""
from restfulcomm.configurations.rabbitmqclientconfig import RabbitMqClientConfig
from restfulcomm.providers.clientprovider import ClientProvider
from examples.examplesettings.rabbitmq import *

message = 'This is my print request example message'

configuration = RabbitMqClientConfig(
        rmq_user=RABBITMQ_USER,
        rmq_password=RABBITMQ_PASSWORD,
        rmq_server=RABBITMQ_SERVER,
        rmq_vhost=RABBITMQ_VHOST,
        rmq_queue=RABBITMQ_QUEUE,
        rmq_delivery=RABBITMQ_DELIVERY_MODE,
        rmq_exchange=RABBITMQ_EXCHANGE
)

provider = ClientProvider('rabbitmq', configuration)

provider.client.request(
        method_='GET',
        resource_='/path/to',
        data_=message,
        headers_={'a': 'first', 'b': 'second'}
)
