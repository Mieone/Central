from django.db import models, IntegrityError
from django.utils import timezone

class SendSms(models.Model):
    number           = models.CharField(max_length=200)
    message          = models.CharField(max_length=200)
    call_back_uri    = models.TextField()
    status_choices   = ((0, 'InProgress'), (1, 'Done'), (2, 'Failed'),)
    status           = models.IntegerField(default=0, blank=True, choices=status_choices)
    dt_added         = models.DateTimeField(default=timezone.now, blank=True)
    def __unicode__(self):
        return "Number: %s -- Message: %s -- call_back_uri: %s" % (self.number, self.message, self.call_back_uri)


