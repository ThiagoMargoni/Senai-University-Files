from .models import *
from .serializer import *
from rest_framework.views import APIView
from rest_framework.response import Response

class LocationAPIView(APIView):
    def get(self, request, id=''):
        try:
            filters = ['name', 'type', 'residents']
            hasFilter = False
            found = ''
            
            for filter in filters:
                if filter in request.GET:
                    routeFilter = request.GET[filter]
                    if found == '':
                        found = Location.objects.filter(
                            **{f'{filter}__contains': routeFilter}
                        )
                    else:
                        found = found.filter(
                            **{f'{filter}__contains': routeFilter}
                        )

                    hasFilter = True
                    

            if hasFilter==False: found = Location.objects.all() if id == '' else Location.objects.get(id=id)
            serializer = LocationSerializer(found, many=True if id == '' else False)
            return Response(serializer.data)
        except Location.DoesNotExist:
            return Response(status=404, data='Location not found!')

    def post(self, request):
        json = request.data

        serialized = LocationSerializer(data=json, many=False)
        if serialized.is_valid():
            serialized.save()
            return Response(status=203, data=serialized.data)
        return Response(status=400, data='Invalid data')
    
    def put(self, request, id=''):
        try:
            found = Location.objects.get(id=id)
            json = request.data
            serialized = LocationSerializer(found, data=json)

            if serialized.is_valid():
                serialized.save()
                return Response(status=200, data='Location successfully updated')

            return Response(status=400, data='Invalid data')

        except Location.DoesNotExist:
            return Response(status=404, data='Location not found!')

    def delete(self, request, id=''):
        try:
            found = Location.objects.get(id=id)
            found.delete()
            return Response(status=200, data='Location successfully delete')

        except Location.DoesNotExist:
            return Response(status=404, data='Location not found!')


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