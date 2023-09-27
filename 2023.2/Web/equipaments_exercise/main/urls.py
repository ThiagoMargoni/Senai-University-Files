from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'equipament', EquipamentAPIView)
router.register(r'comments', CommentsAPIView)

urlpatterns = router.urls

urlpatterns.append(path('comments/order_by_username/<int:id>', CommentsAPIView.order_by_username, name='order_by_username'))