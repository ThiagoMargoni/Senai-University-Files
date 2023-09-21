from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'equipament', EquipamentAPIView)
router.register(r'comment', CommentsAPIView)

urlpatterns = router.urls