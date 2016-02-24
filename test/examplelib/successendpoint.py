"""Example command for parameters printing"""
from restfulcomm.http.jsonresponse import JsonResponse
from restfulcomm.http.superendpoint import Endpoint


class SuccessEndpoint(Endpoint):

    @classmethod
    def PUT(cls, data, **kwargs):
        pass

    @classmethod
    def GET(cls, content):
        json_response = JsonResponse()
        json_response.status = 200
        json_response.body = content
        return json_response

    @classmethod
    def POST(cls, data, **kwargs):
        pass

    @classmethod
    def DELETE(cls, **kwargs):
        pass