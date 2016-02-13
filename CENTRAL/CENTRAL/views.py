from oauth2_provider.views.generic import ProtectedResourceView
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from mieone import  provide_key
from django.utils.decorators import method_decorator
from oauth2_provider.decorators import protected_resource


def home(request):
    return render(request, 'index.html', {})

@provide_key
@protected_resource()
def send_sms(request):
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

    return JsonResponse({'data': data, 'status': msg})
