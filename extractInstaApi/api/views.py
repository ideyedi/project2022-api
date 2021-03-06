from django.http import HttpResponse, JsonResponse
# django REST framework
from rest_framework import views
from .util import crawler


# Create your views here.
class DemoApi(views.APIView):
    instagram_link = 'https://www.instagram.com'
    test_link = 'https://www.instagram.com/p/CfVx-zFvcg7'

    def __init__(self):
        pass

    # /api/extract
    # APIView GET
    def get(self, request):
        #url = request.GET.get('insta_link', default=None)
        #print(url)

        clr = crawler.InstaCrawler(self.test_link)
        clr.login()
        #clr.extract_image()

        return JsonResponse({'name': self.test_link})

    # APIView POST
    def post(self, request):
        return JsonResponse({'post': self.url})


class ViewGrpc(views.APIView):

    def __init__(self):
        pass

    def get(self):
        return 0

