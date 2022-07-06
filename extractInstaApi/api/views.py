from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse

# django REST framework
from rest_framework import views
from rest_framework.response import Response


# Create your views here.
class DemoApi(views.APIView):
    test_link = 'https://www.instagram.com/p/CfVx-zFvcg7'

    def __init__(self):
        pass

    # /api/extract
    # GET method test
    def extract_insta_image(request, insta_link):

        context = {'name': insta_link}
        # render return value is HttpResponse
        ret = render(request, )

        return ret

