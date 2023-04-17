from Denee.models import Event
from rest_framework import serializers


class EventDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
