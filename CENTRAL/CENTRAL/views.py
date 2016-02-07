from oauth2_provider.views.generic import ProtectedResourceView
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

import urllib

def home(request):
    return render(request, 'index.html', {})

class ApiEndpoint(ProtectedResourceView):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, OAuth2!')

class SendSms(ProtectedResourceView):
    def post(self, request):
        number = request.POST.get('number', '')
        message = request.POST.get('message', '')
        if not number:
            return HttpResponse('Please send the number with "number"')
        msg = 'Success'
        url = 'https://control.msg91.com/api/sendhttp.php?authkey=77123ATu6JCJlW3I554a7f9d3&mobiles=%s&message=%s&sender=MIEBAC&route=4'
        url = url %(number, urllib.quote(message))
        try:
            data = urllib.urlopen(url).read()
        except Exception as e:
            data = traceback.format_exc()
            msg = 'Failed'
        #return HttpResponse(msg)
        return JsonResponse({'data': data, 'status': msg})
