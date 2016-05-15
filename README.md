# restfulcomm #

RESTful-like communication Client and a server allowing to 
use RabbitMQ or HTTP Werkzeug alternatively.

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

## Example of use ##

You are developing an application with multiple remote components. 
Some components need to exchange data. So you need a server to 
server communicaton, at least one client and/or one
server for each node.

Implement this client and server and no matters if on begin you 
are using RabbitMQ for messaging and after you want to switch to 
an HTTP API. You can do easily.

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
