# -*- coding: utf-8 -*-
"""Example endpoint for image downloading"""
from restfulcomm.http.superendpoint import Endpoint
from werkzeug.wrappers import Response
from test.examplesettings.globals import TEST_ROOT_PATH


class ImageEndpoint(Endpoint):

    @classmethod
    def GET(cls, request, **kwargs):
        img_path = cls.publish_img_path()

        with open(img_path, 'rb') as img_file:
            img_content = img_file.read()

        return Response(
            response=img_content,
            content_type='image/png'
        )

    @classmethod
    def publish_img_path(cls):
        img_path = '{!s}/examplemedia/python-icon.png'.format(
            TEST_ROOT_PATH
        )
        return img_path

