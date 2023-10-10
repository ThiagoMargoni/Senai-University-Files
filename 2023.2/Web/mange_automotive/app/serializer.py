from .models import *
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','email','is_superuser','first_name','last_login')
        many = True

class MyUserSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = MyUser
        fields = '__all__'
        many = True

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'
        many = True

class  ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        many = True

class AutomobileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Automobile
        fields = '__all__'
        many = True

class AvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Availability
        fields = '__all__'
        many = True
    
class MaintenanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maintenance
        fields = '__all__'
        many = True

class MaintenanceServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenanceService
        fields = '__all__'
        many = True

class MaintenanceProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenanceProduct
        fields = '__all__'
        many = True

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
        many = True