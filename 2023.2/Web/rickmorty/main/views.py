from .models import *
from .serializer import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated

class LocationAPIView(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'type', 'dimension', 'created']
    permission_classes = (IsAuthenticated, )

class EpisodeAPIView(APIView):
    def get(self, request, id=''):
        try:
            found = Episode.objects.all() if id == '' else Episode.objects.get(id=id)
            serializer = EpisodeSerializer(found, many=True if id == '' else False)
            return Response(serializer.data)
        except Episode.DoesNotExist:
            return Response(status=404, data='Episode not found!')
        
    def post(self, request):
        json = request.data

        serialized = EpisodeSerializer(data=json, many=False)
        if serialized.is_valid():
            serialized.save()
            return Response(status=203, data=serialized.data)
        return Response(status=400, data='Invalid data')
    
    def put(self, request, id=''):
        try:
            found = Episode.objects.get(id=id)
            json = request.data
            serialized = EpisodeSerializer(found, data=json)

            if serialized.is_valid():
                serialized.save()
                return Response(status=200, data='Episode successfully updated')

            return Response(status=400, data='Invalid data')

        except Episode.DoesNotExist:
            return Response(status=404, data='Episode not found!')

    def delete(self, request, id=''):
        try:
            found = Episode.objects.get(id=id)
            found.delete()
            return Response(status=200, data='Episode successfully delete')

        except Episode.DoesNotExist:
            return Response(status=404, data='Episode not found!')
    
class CharacterAPIView(APIView):
    def get(self, request, id=''):
        try:
            found = Character.objects.all() if id == '' else Character.objects.get(id=id)
            serializer = CharacterSerializer(found, many=True if id == '' else False)
            return Response(serializer.data)
        except Location.DoesNotExist:
            return Response(status=404, data='Character not found!')
        
    def post(self, request):
        json = request.data
        serialized = CharacterSerializer(data=json, many=False)
        if serialized.is_valid():
            serialized.save()
            return Response(status=203, data=serialized.data)
        return Response(status=400, data='Invalid data')
    
    def put(self, request, id=''):
        try:
            found = Character.objects.get(id=id)
            json = request.data
            serialized = CharacterSerializer(found, data=json)

            if serialized.is_valid():
                serialized.save()
                return Response(status=200, data='Character successfully updated')

            return Response(status=400, data='Invalid data')

        except Character.DoesNotExist:
            return Response(status=404, data='Character not found!')
    
    def delete(self, request, id=''):
        try:
            found = Character.objects.get(id=id)
            found.delete()
            return Response(status=200, data='Character successfully delete')

        except Character.DoesNotExist:
            return Response(status=404, data='Character not found!')