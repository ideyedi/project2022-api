from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse

# django REST framework
from rest_framework.response import Response
from rest_framework import views
from rest_framework.response import Response


# Create your views here.
class DemoApi(views.APIView):
    test_link = 'https://www.instagram.com/p/CfVx-zFvcg7'
    # example 'https://scontent-ssn1-1.cdninstagram.com/v/t51.2885-15/291118957_421835559823293_4126431104790276899_n.jpg?stp=dst-jpg_e35_p1080x1080&_nc_ht=scontent-ssn1-1.cdninstagram.com&_nc_cat=1&_nc_ohc=vUUG6mjB_wIAX9uXrIf&edm=ALQROFkBAAAA&ccb=7-5&ig_cache_key=Mjg3MDQyMDE1MzAxNzY3MDc4MQ%3D%3D.2-ccb7-5&oh=00_AT_d2DKJYHyG3yCe2McnHb8HkKoZHtzhCFSmORvuTJ2bKQ&oe=62C628D2&_nc_sid=30a2ef'
    
    # /api/extract
    # GET method test
    def get(self, *args):
        temp = {'name': '지은석', '이름': '김정우'}
        return JsonResponse(temp)

