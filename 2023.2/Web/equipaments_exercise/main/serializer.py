from rest_framework import serializers
from .models import *

class EquipamentSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = Equipament
        fields = '__all__'

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = Comment
        fields = '__all__'