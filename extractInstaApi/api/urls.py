from django.urls import re_path
from .views import (DemoApi,)

app_name = 'api'

urlpatterns = [
    re_path(r'^extract/', DemoApi.as_view(), name='extract'),
]
