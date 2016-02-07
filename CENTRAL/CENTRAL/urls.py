from django.conf.urls import url, include
from django.contrib import admin
from .views import ApiEndpoint, SendSms, home
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^api/hello', ApiEndpoint.as_view()),
    url(r'^api/sendsms', csrf_exempt(SendSms.as_view())),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login')
]
