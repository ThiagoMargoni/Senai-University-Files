from .models import *
from .serializer import *
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from .filters import *
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissionsOrAnonReadOnly, SAFE_METHODS
from django.db.models import F, Sum

from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

# pip install djangorestframework-composed-permissions
from restfw_composed_permissions.base import BaseComposedPermission

class UserReadOnly(BaseComposedPermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.method in SAFE_METHODS
        return False
    
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        return False
    
class AuthorAndAdminOrReadOnly(BaseComposedPermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.method in SAFE_METHODS
        return False
    
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True

        if obj.userFk.user == request.user.id:
            return True
        
        return False

class CreateUserPermission(BaseComposedPermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS or request.method == 'POST'
    
    def has_object_permission(self, request, view, obj):
        if MyUser.objects.filter(user=request.user.id).values('type') == "M":
            return True
        
        return False

class IsMasterOrReadOnly(BaseComposedPermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS
    
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True

        if obj.user.id == request.user.id:
            return True
        
        return False

class MyUserView(ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = '__all__'
    filterset_class = MyUserFilter
    permission_classes = (CreateUserPermission, )
    
    def get_queryset(self):
        user = self.request.user
        queryset = None
        if user.is_superuser:
            queryset = MyUser.objects.all()
        else:
            queryset = MyUser.objects.filter(user__username=user.username)
        return queryset 

class ServiceView(ModelViewSet):
    queryset = Service.objects.all()
    serializer_class =  ServiceSerializer
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = '__all__'
    filterset_class = ServiceFilter
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)

class ProductView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = '__all__'
    filterset_class = ProductFilter
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)

    @action(detail=False, methods=['GET'])
    def get_five_less(self, request):
        user = self.request.user
        user_role = MyUser.objects.filter(user=user.id).values('type')
        if user_role == 'M':
            found = Product.objects.filter(quantity__lte=5)
            serializer = ProductSerializer(found, many=True)
            return Response(serializer.data)
        else:
            return Response(status=401, data='Permissions denied')
        
class AutomobileView(ModelViewSet):
    queryset = Automobile.objects.all()
    serializer_class = AutomobileSerializer
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = '__all__'
    filterset_class = AutomobileFilter
    permission_classes = (IsAuthenticated,)

class AvailabilityView(ModelViewSet):
    queryset = Availability.objects.all()
    serializer_class = AvailabilitySerializer
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = '__all__'
    filterset_class = AvailabilityFilter
    permission_classes = (IsMasterOrReadOnly,)

    # def create(self, request, *args, **kwargs):
    #     ...

    # def update(self, request, *args, **kwargs):
    #     ...

class MaintenanceView(ModelViewSet):
    queryset = Maintenance.objects.all()
    serializer_class = MaintenanceSerializer
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = '__all__'
    filterset_class = MaintenanceFilter
    permission_classes = (AuthorAndAdminOrReadOnly,)

    def get_queryset(self):
        user = self.request.user
        queryset = None
        if user.is_superuser:
            queryset = Maintenance.objects.all()
        else:
            queryset = Maintenance.objects.filter(maintenanceFk__userFk__user__username=user.username)
        return queryset 

    def create(self, request, *args, **kwargs):
        data = request.data

        if data['dropoff_date'].is_available:
            
            response = super(MaintenanceView, self).create(request,*args,**kwargs)

            if response.status_code == 201:
                Availability.objects.filter(id=data['dropoff_date']).update(status='U')   
                return Response(status=201,data=response.data)
            else:
                return Response(status=500,data='Error when saving the maintenance booking!')
        else:
            return Response(status=403, data='This date/station is unavailable')
    
    def update(self, request, *args, **kwargs):
        data = request.data

        if data['dropoff_date'].is_available:
            old_date = Maintenance.objects.filter(id=data['id']).values('dropoff_date')
            response = super(MaintenanceView, self).update(request,*args,**kwargs)

            if response.status_code == 201:
                Availability.objects.filter(id=data['dropoff_date']).update(status='U')
                Availability.objects.filter(id=old_date).update(status='A')
                return Response(status=201,data=response.data)
            else:
                return Response(status=500,data='Error when saving the update of the maintenance booking!')
        else:
            return Response(status=403, data='This date/station is unavailable')
    
class MaintenanceServiceView(ModelViewSet):
    queryset = MaintenanceService.objects.all()
    serializer_class = MaintenanceServiceSerializer
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = '__all__'
    filterset_class = MaintenanceServiceFilter
    permission_classes = (UserReadOnly,)

    def get_queryset(self):
        user = self.request.user
        queryset = None
        if user.is_superuser:
            queryset = MaintenanceService.objects.all()
        else:
            queryset = MaintenanceService.objects.filter(maintenanceFk__userFk__user__username=user.username)
        return queryset 

class MaintenanceProductView(ModelViewSet):
    queryset = MaintenanceProduct.objects.all()
    serializer_class = MaintenanceProductSerializer
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = '__all__'
    filterset_class = MaintenanceProductFilter
    permission_classes = (UserReadOnly,)

    def create(self, request, *args, **kwargs):
        data = request.data

        if data['quantity'] <= Product.objects.filter(id=data['productFk']).values('quantity') or data['quantity'] == 0:
            response = super(MaintenanceProductView, self).create(request,*args,**kwargs)

            if response.status_code == 201:  
                Product.objects.filter(id=data['productFk']).update(quantity=F('quantity') - data['quantity']) 
                return Response(status=201,data=response.data)
            else:
                return Response(status=500,data='Error when saving the product in the maintenance!')
        else:
            return Response(status=403, data='The quantity cannot be zero or greater than available')
        
    def update(self, request, *args, **kwargs):
        data = request.data

        if data['quantity'] <= Product.objects.filter(id=data['productFk']).values('quantity') or data['quantity'] == 0:
            
            old_quantity = MaintenanceProduct.objects.filter(id=data['id']).values('quantity')
            Product.objects.filter(id=data['productFk']).update(quantity=F('quantity') + old_quantity)
            response = super(MaintenanceProductView, self).update(request,*args,**kwargs)

            if response.status_code == 201:   
                Product.objects.filter(id=data['productFk']).update(quantity=F('quantity') - data['quantity'])
                return Response(status=201,data=response.data)
            else:
                Product.objects.filter(id=data['productFk']).update(quantity=F('quantity') - old_quantity)
                return Response(status=500,data='Error when saving the update of the product in the maintenance!')
        else:
            return Response(status=403, data='The quantity cannot be zero or greater than available')
        
    def get_queryset(self):
        user = self.request.user
        queryset = None
        if user.is_superuser:
            queryset = MaintenanceProduct.objects.all()
        else:
            queryset = MaintenanceProduct.objects.filter(maintenanceFk__userFk__user__username=user.username)
        return queryset 
 
class PaymentView(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = '__all__'
    filterset_class = PaymentFilter
    permission_classes = (UserReadOnly,)

    def create(self, request, *args, **kwargs):
        data = request.data

        total = 0.0
        total += MaintenanceProduct.objects.filter(maintenanceFk = data['maintenanceFk']).aggregate(Sum('total'))
        total += MaintenanceService.objects.filter(maintenanceFk = data['maintenanceFk']).aggregate(Sum('total'))

        data['total'] = total

        response = super(PaymentView, self).create(request, *args,**kwargs)

        if response.status_code == 201:
            return Response(status=201,data=response.data)
        else:
            return Response(status=500,data='Error when saving the payment of the maintenance!')
        
    def update(self, request, *args, **kwargs):
        data = request.data

        total = 0.0
        total += MaintenanceProduct.objects.filter(maintenanceFk = data['maintenanceFk']).aggregate(Sum('total'))
        total += MaintenanceService.objects.filter(maintenanceFk = data['maintenanceFk']).aggregate(Sum('total'))

        data['total'] = total

        response = super(PaymentView, self).update(request, *args,**kwargs)

        if response.status_code == 201:
            return Response(status=201,data=response.data)
        else:
            return Response(status=500,data='Error when saving the payment update!')
        
    def get_queryset(self):
        user = self.request.user
        queryset = None
        if user.is_superuser:
            queryset = Payment.objects.all()
        else:
            queryset = Payment.objects.filter(maintenanceFk__userFk__user__username=user.username)
        return queryset 