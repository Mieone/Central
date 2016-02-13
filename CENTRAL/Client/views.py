from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from Client.models_serialization import SendSmsSerializer
from rest_framework.parsers import JSONParser
from django.conf import settings
from django_mailer import send_mail
from mieone import  provide_key
from oauth2_provider.decorators import protected_resource

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

#Which saves the data in sendsms table, later scheduler will send the sms
@provide_key
@protected_resource()
def sendsms(request):
    data = {"number": request.POST.get('number', ''),
            "message": request.POST.get('message', ''),
            "call_back_uri": request.POST.get('call_back_uri', '')}
    serializer = SendSmsSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JSONResponse(serializer.data, status=201)
    return JSONResponse(serializer.errors, status=400)

#Django_mailer will store this data into django_mailer_message table and scheduler will send the mails
@provide_key
@protected_resource()
def sendmail(request):
    title = request.POST.get('title', '')
    mail_data = request.POST.get('message', '')
    to        = request.POST.get('to', '')
    if "," in to:
        to = [i.strip() for i in to.split(",") if i.strip()]
    elif to:
        to = [to.strip()] if to.strip() else ''
    else:
        return JSONResponse("To Address should not be empty", status=201)
    try:
        send_mail(title, mail_data, settings.DEFAULT_FROM_EMAIL, to)
        return JSONResponse({'Status': 'Success'}, status=201)
    except:
        return JSONResponse({'Status': 'Failed'}, status=201)
