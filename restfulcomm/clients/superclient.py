"""Super client class"""
from abc import ABCMeta, abstractmethod


class CommClient(metaclass=ABCMeta):

    METHOD_GET = 'GET'
    METHOD_POST = 'POST'
    METHOD_PUT = 'PUT'
    METHOD_DELETE = 'DELETE'

    @abstractmethod
    def __init__(self, configuration):
        """Configures the request components and initializes the instance.

        Args:
            configuration: Config server configuration object
        """
        self._configuration = configuration
        pass

    @abstractmethod
    def request(self, method_, resource_, data_, headers_):
        """Request the components to server and return the response.

        Args:
            method_: str GET | POST | PUT | DELETE
            resource_: str
            data_: dict
            headers_: dict
        """
        pass
