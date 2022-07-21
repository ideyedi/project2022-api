from django.urls import re_path
from .views import (DemoApi,
                    ViewGrpc,
                    )

app_name = 'api'

urlpatterns = [
    re_path(r'^extract', DemoApi.as_view(), name='extract'),
    re_path(r'^testgrpc', ViewGrpc.as_view(), name='grpc'),
]
