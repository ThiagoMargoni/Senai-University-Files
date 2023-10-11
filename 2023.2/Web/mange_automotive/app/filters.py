from rest_framework import filters
import django_filters
from django_filters import FilterSet
from .models import *

class MyUserFilter(FilterSet):
    type = django_filters.CharFilter(lookup_expr='icontains')
    address = django_filters.CharFilter(lookup_expr='icontains')
    phone_number = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = MyUser
        fields = ['type', 'address', 'phone_number']

class ServiceFilter(FilterSet):
    service_type = django_filters.CharFilter(lookup_expr='icontains')
    service_price = django_filters.RangeFilter()

    class Meta:
        model = Service
        fields = ['service_type', 'service_price']

class ProductFilter(FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    quantity_in_stock = django_filters.RangeFilter()
    producer_name = django_filters.CharFilter(lookup_expr='icontains')
    producer_key = django_filters.CharFilter(lookup_expr='icontains')
    purchase_price = django_filters.RangeFilter()
    sale_price = django_filters.RangeFilter()

    class Meta:
        model = Product
        fields = ['name', 'quantity_in_stock', 'producer_name', 'producer_key', 'purchase_price', 'sale_price']

class AutomobileFilter(FilterSet):
   type = django_filters.CharFilter(lookup_expr='icontains')
   brand = django_filters.CharFilter(lookup_expr='icontains')
   model = django_filters.CharFilter(lookup_expr='icontains')
   year = django_filters.RangeFilter()

   class Meta:
       model = Automobile
       fields = ['type', 'brand', 'model', 'year']

class AvailabilityFilter(FilterSet):
    status = django_filters.CharFilter(lookup_expr='icontains')
    station = django_filters.CharFilter(lookup_expr='icontains')
    date = django_filters.RangeFilter()

    class Meta:
        model = Availability
        fields = ['status', 'station', 'date']

class MaintenanceFilter(FilterSet):
    userFk = django_filters.NumberFilter(lookup_expr='iexact')
    automobileFk = django_filters.NumberFilter(lookup_expr='iexact')
    dropoff_date = django_filters.RangeFilter(field_name='dropoff_date__date')
    pickup_date = django_filters.RangeFilter()
    status = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Maintenance
        fields = ['userFk', 'automobileFk', 'dropoff_date', 'pickup_date', 'status']

class MaintenanceServiceFilter(FilterSet):
    maintenanceFk = django_filters.NumberFilter(lookup_expr='iexact')
    serviceFk = django_filters.NumberFilter(lookup_expr='iexact')
    employeeFk = django_filters.NumberFilter(lookup_expr='iexact')
    total = django_filters.RangeFilter()

    class Meta:
        model = MaintenanceService
        fields = ['maintenanceFk', 'serviceFk', 'employeeFk', 'total']

class MaintenanceProductFilter(FilterSet):
    maintenanceFk = django_filters.NumberFilter(lookup_expr='iexact')
    productFk = django_filters.NumberFilter(lookup_expr='iexact')
    quantity = django_filters.RangeFilter()
    total = django_filters.RangeFilter()

    class Meta:
        model = MaintenanceService
        fields = ['maintenanceFk', 'productFk', 'quantity', 'total']

class PaymentFilter(FilterSet):
    type_payment = django_filters.CharFilter(lookup_expr='icontains')
    maintenanceFk = django_filters.NumberFilter(lookup_expr='iexact')
    discount = django_filters.RangeFilter()
    total = django_filters.RangeFilter()
    total_discount = django_filters.RangeFilter()
    status = django_filters.CharFilter(lookup_expr='icontains')