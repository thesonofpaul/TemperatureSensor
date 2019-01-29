from rest_framework import viewsets
from .serializers import AccountSerializer, TempSensorHistorySerializer, ConfigurationSerializer
from .models import Account, TempSensorHistory, Configuration

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class TempSensorHistoryViewSet(viewsets.ModelViewSet):
    queryset = TempSensorHistory.objects.all()
    serializer_class = TempSensorHistorySerializer

class ConfigurationViewSet(viewsets.ModelViewSet):
    queryset = Configuration.objects.all()
    serializer_class = ConfigurationSerializer
