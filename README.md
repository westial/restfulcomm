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
