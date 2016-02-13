from rest_framework import serializers
from models import SendSms

class SendSmsSerializer(serializers.Serializer):
    sno = serializers.IntegerField(read_only=True)
    number = serializers.CharField(required=True, allow_blank=False, max_length=100)
    message = serializers.CharField(required=True, allow_blank=False, max_length=512)
    call_back_uri = serializers.CharField(required=False, allow_blank=True, max_length=2048)
    status = serializers.ChoiceField(choices=((0, 'InProgress'), (1, 'Done'), (2, 'Failed'),), default=0)
    reference_id = serializers.CharField(required=False, allow_blank=True, max_length=2048)
    dt_added = serializers.DateTimeField(required=False)
    dt_updated = serializers.DateTimeField(required=False)

    def create(self, validated_data):
        """
        Create and return a new `SendSms` instance, given the validated data.
        """
        return SendSms.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `SendSms` instance, given the validated data.
        """
        instance.number = validated_data.get('number', instance.number)
        instance.message = validated_data.get('message', instance.message)
        instance.call_back_uri = validated_data.get('call_back_uri', instance.call_back_uri)
        instance.reference_id = validated_data.get('reference_id', instance.reference_id)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance

