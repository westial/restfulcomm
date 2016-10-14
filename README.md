# restfulcomm #

RESTful-like Server and Clients with RabbitMQ and HTTP Werkzeug support.

## Requirements ##

### OS ###

* Python 3.4
* RabbitMQ Server

### Python packages ###

* werkzeug
* pika
* requests

## Installation ##

`$ python3 setup.py install`

## Usage ##

Check the /test directory, there are some functional test cases which
can help your implementation.

## Why you would need that component ##

For example, your project is a microservices based application. The 
nodes are requesting the services through RESTful HTTP interfaces. May 
be somewhere is more appropriate a RabbitMQ based communication, and
you would have to program its interfaces and clients...

Implement this restfulcomm client and server in your interfaces and
let this communication infrastructure do the job. No matters if you 
start using RabbitMQ for messaging and after you want to switch to 
an HTTP API.

## Full example ##

Basic example source code for context with both servers, HTTP and RMQ,
both clients and a request example script to make it easy. I don't
trust that the following works, see the test directory examples for 
full working examples.

### endpoint.py ###

Define an endpoint. Available for both HTTP and RMQ clients.

```
from restfulcomm.http.superendpoint import Endpoint
from restfulcomm.resources.basicserverresource import BasicServerResource
from werkzeug.wrappers import Response


class BounceEndpoint(Endpoint):

    @classmethod
    def GET(cls, request, **kwargs):
    """Bounce content"""
        content = kwargs['content']
        return Response(content)
        
bounce_endpoint_resource = BasicServerResource(
    BounceEndpoint,
    '/index/<content>',
    route_defaults
)
```

### http_server.py ###

Configure the HTTP server properties, attach the endpoint and start 
listening.

```
from endpoint import bounce_endpoint_resource

configuration = WerkzeugServerConfig(
    web_user=None,
    web_password=None,
    web_server='127.0.0.1',
    web_port=5000,
    use_debugger=True,
    use_reloader=False
)

server_provider = ServerProvider(
        'werkzeug',
        [bounce_endpoint_resource],
        configuration
)

cls.set_server(server_provider.server)
cls._server().listen()
```

### rabbitmq_server.py ###

Configure the RMQ server properties, attach the endpoint and start 
listening.

```
configuration = RabbitMqServerConfig(
        rmq_user='guest',
        rmq_password='password',
        rmq_server='127.0.0.1',
        rmq_vhost='/',
        rmq_queue='sample',
        rmq_prefetch=1,
        rmq_exchange=''
)

server_provider = ServerProvider(
        'rabbitmq',
        [bounce_endpoint_resource],
        configuration
)

cls.set_server(server_provider.server)
cls._server().listen()
```

### http_client.py ###

At this point, if the HTTP server above is listening, we can use 
this HTTP client to write from any node to the HTTP server.

```
configuration = WerkzeugClientConfig(
        web_user=None,
        web_password=None,
        web_scheme='http',
        web_server='127.0.0.1',
        web_port=5000,
        web_timeout=30
)

provider = ClientProvider('werkzeug', configuration)

http_client = provider.client
```

### rabbitmq_client.py ###

Same thing for RabbitMQ: if the RMQ server above is listening, this
RMQ client below writes from any node to the RMQ server.

```
configuration = RabbitMqClientConfig(
        rmq_user='guest',
        rmq_password='password',
        rmq_server='127.0.0.1',
        rmq_vhost='/',
        rmq_queue='sample',
        rmq_delivery=2,
        rmq_exchange='',
        rmq_timeout=60
)
provider = ClientProvider('rabbitmq', configuration)

rabbit_client = provider.client
```

### request_example.py ###

```
# The request below works for both clients, HTTP and RMQ. 
# import the appropriate client and request to the endpoint.

json_response = any_client.do_request(
        method='GET',
        resource='/index/bouncing-content'
)

assert json_response.status == 200
```

## License ##

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
