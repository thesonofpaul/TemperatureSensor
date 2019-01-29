from rest_framework import serializers
from .models import Account, TempSensorHistory, Configuration

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

class TempSensorHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TempSensorHistory
        fields = '__all__'

class ConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Configuration
        fields = '__all__'