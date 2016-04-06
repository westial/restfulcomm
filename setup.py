from distutils.core import setup

version_file = open('VERSION', 'r')
version = version_file.readline()

setup(
    name='restfulcomm',
    version=version,
    packages=['restfulcomm', 'restfulcomm.core', 'restfulcomm.http',
              'restfulcomm.clients', 'restfulcomm.servers',
              'restfulcomm.services', 'restfulcomm.providers',
              'restfulcomm.resources', 'restfulcomm.configurations'],
    url='https://github.com/westial/restfulcomm',
    license='GPL v3',
    author='Jaume Mila',
    author_email='jaume@westial.com',
    description='Client and a server to manage a RESTful-like communication '
                'allowing to switch the medium between RabbitMQ and HTTP '
                'Werkzeug.',
    install_requires=[
        'werkzeug',
        'pika',
        'requests'
    ]
)
