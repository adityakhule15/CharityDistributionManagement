from .models import Admin
from rest_framework import serializers


class AdminDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'
