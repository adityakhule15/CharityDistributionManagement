from Denee.models import Doner
from rest_framework import serializers


class DonerDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doner
        fields = '__all__'
