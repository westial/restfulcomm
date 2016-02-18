"""Server worker"""
from examples.rabbitmq_to_json_response.convertjsontoresponsecommand import \
    ConvertJsonToResponseCommand
from restfulcomm.configurations.rabbitmqserverconfig import \
    RabbitMqServerConfig
from restfulcomm.providers.serverprovider import ServerProvider
from examples.examplesettings.rabbitmq import *

configuration = RabbitMqServerConfig(
        rmq_user=RABBITMQ_USER,
        rmq_password=RABBITMQ_PASSWORD,
        rmq_server=RABBITMQ_SERVER,
        rmq_vhost=RABBITMQ_VHOST,
        rmq_queue=RABBITMQ_QUEUE,
        rmq_prefetch=RABBITMQ_PREFETCH_COUNT,
        rmq_exchange=RABBITMQ_EXCHANGE
)

ServerProvider(
        'rabbitmq',
        ConvertJsonToResponseCommand,
        configuration
).server.listen()
