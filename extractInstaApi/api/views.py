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
    def get(self, request, insta_link):
        context = {'name': insta_link}

        return JsonResponse(context)


    def post(self, request):
        return 0