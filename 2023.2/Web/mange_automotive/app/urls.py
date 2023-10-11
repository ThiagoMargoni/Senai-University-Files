from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'user', MyUserView)
router.register(r'service', ServiceView)
router.register(r'product', ProductView)
router.register(r'automobile', AutomobileView)
router.register(r'availability', AvailabilityView)
router.register(r'maintenance', MaintenanceView)
router.register(r'maintenance_service', MaintenanceServiceView)
router.register(r'maintenance_product', MaintenanceProductView)
router.register(r'payment', PaymentView)

urlpatterns = router.urls