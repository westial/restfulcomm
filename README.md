# restfulcomm #

Client and a server to manage a RESTful-like communication allowing to 
switch the medium between RabbitMQ and HTTP Werkzeug.

RabbitMQ and HTTP Werkzeug client and server implement an abstract class
and are limited by its contracts.

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
can help you for implementation.

## Example of use ##

You are developing an application with multiple components. Some 
components need to connect remotely and exchange data. So you need
a client in one side and a server in the other, even you may need a
server and a client twice for both directions. 

Implement this provided client and server and no matters if on begin 
you use RabbitMQ queues for messaging and after you want to switch to 
an HTTP API. Switching between them is so easy as configure the client
and server in both sides.

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