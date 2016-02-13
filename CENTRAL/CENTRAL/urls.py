from django.conf.urls import url, include
from django.contrib import admin
from .views import send_sms, home
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^api/sendsms', csrf_exempt(send_sms), name='send_sms'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^api_calls', include('Client.urls', namespace='Client')),
]
