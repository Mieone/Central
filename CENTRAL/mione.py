import requests
import json
import os
import sys
import urllib

sys.path.append('~/CENTRAL')
sys.path.append('~/CENTRAL/CENTRAL')
os.environ['DJANGO_SETTINGS_MODULE'] = 'CENTRAL.settings'
from django.http import HttpResponse
from django.conf import settings
from Client.models import SendSms
from Client.models_serialization import SendSmsSerializer
from rest_framework.parsers import JSONParser
MSG1 = "Unable to get the token pls check the secret, id, and token url"
MSG2 = "Please Mention proper client id and proper client secret else use_default=True"

class AppData(object):
    def __init__(self, **kwargs):
        self.app_id = kwargs.get('app_id', settings.CENTRAL_APP_ID)
        self.app_secret = kwargs.get('app_secret', settings.CENTRAL_APP_SECRET)
        self.grant_type = kwargs.get('app_grant_type', settings.CENTRAL_APP_GRANT_TYPE)
        self.token_url = kwargs.get('app_token_url', settings.CENTRAL_TOKEN_URL)
        self.get_json = {'grant_type': self.grant_type, 'redirect_uri': self.token_url,
                        'client_id': self.app_id, 'client_secret': self.app_secret }

    def get_token(self):
        token = ''
        try:
            response = json.loads((requests.post(self.token_url, data=self.get_json)).text)
            token = " ".join([response['token_type'], response['access_token']])
        except:
            token = MSG1
        return token

    def generate_key(self, client_id='', client_secret='', use_default=True):
        print client_id, client_secret
        if (not client_id or not client_secret) and not use_default:
            return MSG2
        elif client_id and client_secret:
            self.app_id = client_id
            self.app_secret = client_secret

        return self.get_token()

class MieOne(AppData):
    def __init__(self):
        AppData.__init__(self)
        self.app_token =  self.generate_key()

    def get_my_token(self):
        return self.app_token

def provide_key(f):
    def return_fun(request, *args, **kwargs):
        c_id = request.POST.get('client_id')
        c_secret = request.POST.get('client_secret')
        obj = AppData(app_id = c_id, app_secret = c_secret)
        key = obj.generate_key()
        print key
        if key not in [MSG1, MSG2]:
            request.META['HTTP_AUTHORIZATION'] = key
            return f(request, *args, **kwargs)
        else:
            return HttpResponse(MSG1)
    #return_fun.__doc__=f.__doc__
    #return_fun.__name__=f.__name__
    return return_fun

def sendsms():
    records = SendSms.objects.filter(status=0)
    for rec in records:
        s_rec = SendSmsSerializer(rec)
        r_data = s_rec.data
        r_data['status'] = 1
        url = 'https://control.msg91.com/api/sendhttp.php?authkey=77123ATu6JCJlW3I554a7f9d3&mobiles=%s&message=%s&sender=MIEBAC&route=4'
        url = url %(r_data['number'], urllib.quote(r_data['message']))
        try:
            data = urllib.urlopen(url).read()
            r_data['reference_id']  = data
        except Exception as e:
            data = traceback.format_exc()
	    r_data['status'] = 2

        s_rec.update(rec, r_data)
        r_url = ''
        try:
            if r_data['call_back_uri']:
                r_url = r_data['call_back_uri'] + "?status=%s&Sno=%s&referenceid=%s" % (r_data['status'], r_data['sno'], r_data['reference_id'])
                print r_url
                data = urllib.urlopen(r_url).read()
        except:
            data = traceback.format_exc()
            print r_url
            print "unable to send the response"

