from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt
from .views import *

urlpatterns =[
        url(r'sendsms/$', csrf_exempt(sendsms), name='sendsms'),
        url(r'sendmail/$', csrf_exempt(sendmail), name='sendmail'),
        ]
