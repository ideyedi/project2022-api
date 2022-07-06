from django.http import HttpResponse, JsonResponse
# django REST framework
from rest_framework import views
from .util import crawler


# Create your views here.
class DemoApi(views.APIView):
    test_link = 'https://www.instagram.com/p/CfVx-zFvcg7'

    def __init__(self):
        pass

    # /api/extract
    # GET method test
    def get(self, request):
        #print(help(request))
        url = request.GET.get('insta_link', default=None)
        print(url)

        return JsonResponse({'name': url})

    def post(self, request):
        return 0