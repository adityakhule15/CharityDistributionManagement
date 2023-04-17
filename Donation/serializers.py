from Denee.models import Donation
from rest_framework import serializers


class DonationDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = '__all__'
