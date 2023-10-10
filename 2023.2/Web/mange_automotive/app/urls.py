from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'user', MyUserAPIView)
router.register(r'service', ServiceAPIView)
router.register(r'product', ProductAPIView)
router.register(r'automobile', AutomobileAPIView)
router.register(r'availability', AvailabilityAPIView)
router.register(r'maintenance', MaintenanceAPIView)
router.register(r'maintenance_service', MaintenanceServiceAPIView)
router.register(r'maintenance_product', MaintenanceProductAPIView)
router.register(r'payment', PaymentAPIView)

urlpatterns = router.urls