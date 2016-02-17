"""Entry point for server resources"""
from restfulcomm.servers.rabbitmqserver import RabbitMqCommServer


class ServerProvider(object):
    """Server provider"""

    def __init__(self, server_type, command_class, configuration):
        """Configure a server by the given type and the command class

        Args:
            server_type: str. By the moment only rabbitmq value is allowed.
            command_class: ServerCommand class
            configuration: Config server configuration object

        Raises:
            TypeError if server_type is an unexpected value.
        """
        if server_type == 'rabbitmq':
            server_class = RabbitMqCommServer
        else:
            raise TypeError('Unexpected server type')

        self._server = self.factory(server_class, command_class, configuration)

    @property
    def server(self):
        return self._server

    @classmethod
    def factory(cls, server_class, command_class, configuration):
        return server_class(command_class, configuration)
