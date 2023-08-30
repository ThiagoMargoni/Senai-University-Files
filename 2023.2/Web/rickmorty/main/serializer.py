from rest_framework import serializers
from .models import *

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = Location
        fields = '__all__'

class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = Episode
        fields = '__all__'

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = Character
        fields = '__all__'