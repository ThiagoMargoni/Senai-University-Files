from .models import *
from .serializer import *
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from .filters import *
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissionsOrAnonReadOnly, IsAdminUser

from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.pagination import PageNumberPagination

class MyUserAPIView(ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = '__all__'
    filterset_class = MyUserFilter

class ServiceAPIView(ModelViewSet):
    queryset = Service.objects.all()
    serializer_class =  ServiceSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = '__all__'
    filterset_class = ServiceFilter
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly, )

class ProductAPIView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = '__all__'
    filterset_class = ProductFilter
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly, )

class AutomobileAPIView(ModelViewSet):
    queryset = Automobile.objects.all()
    serializer_class = AutomobileSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = '__all__'
    filterset_class = AutomobileFilter
    permission_classes = (IsAuthenticated)

class AvailabilityAPIView(ModelViewSet):
    queryset = Availability.objects.all()
    serializer_class = AvailabilitySerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = '__all__'
    filterset_class = AvailabilityFilter
    permission_classes = (IsAuthenticated)

class MaintenanceAPIView(ModelViewSet):
    queryset = Maintenance.objects.all()
    serializer_class = MaintenanceSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = '__all__'
    filterset_class = MaintenanceFilter
    permission_classes = (IsAdminUser)

class MaintenanceServiceAPIView(ModelViewSet):
    queryset = MaintenanceService.objects.all()
    serializer_class = MaintenanceServiceSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = '__all__'
    filterset_class = MaintenanceServiceFilter
    permission_classes = (IsAdminUser)

class MaintenanceProductAPIView(ModelViewSet):
    queryset = MaintenanceProduct.objects.all()
    serializer_class = MaintenanceProductSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = '__all__'
    filterset_class = MaintenanceProductFilter
    permission_classes = (IsAdminUser)

class PaymentAPIView(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = '__all__'
    filterset_class = PaymentFilter
    permission_classes = (IsAdminUser)