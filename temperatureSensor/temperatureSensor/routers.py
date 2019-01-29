from rest_framework import routers
from webApp.viewsets import AccountViewSet, TempSensorHistoryViewSet, ConfigurationViewSet

router = routers.DefaultRouter()
router.register(r'account', AccountViewSet)
router.register(r'tempsensorhistory', TempSensorHistoryViewSet)
router.register(r'configuration', ConfigurationViewSet)