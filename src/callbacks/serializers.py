from rest_framework import serializers
from .models import Callback


class CallbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Callback
        fields = ('id', 'received', 'device', 'snr', 'data', 'time')
