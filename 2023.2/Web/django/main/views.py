from .models import *
from .serializer import *
from rest_framework.views import APIView
from rest_framework.response import Response

class PeopleAPIView(APIView):
    def get(self, request, id = ''):
        peopleFound = People.objects.all() if id == '' else People.objects.get(id=id)
        serializer = PeopleSerializer(peopleFound, many=True if id == '' else False)
        return Response(serializer.data)
    
class PlanetAPIView(APIView):
    def get(self, request, id = ''):
        planetFound = Planet.objects.all() if id == '' else Planet.objects.get(id=id)
        serializer = PlanetSerializer(planetFound, many=True if id == '' else False)
        return Response(serializer.data)

class StarshipAPIView(APIView):
    def get(self, request, id = ''):
        starshipFound = Starships.objects.all() if id == '' else Starships.objects.get(id=id)
        serializer = StarshipsSerializer(starshipFound, many=True if id == '' else False)
        return Response(serializer.data)