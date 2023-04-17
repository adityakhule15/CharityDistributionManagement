from Denee.models import Login
from rest_framework import serializers

''' Taking Executive Login Details '''
class LoginDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = '__all__'

