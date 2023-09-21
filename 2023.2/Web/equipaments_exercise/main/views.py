from .models import *
from .serializer import *
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissionsOrAnonReadOnly

class EquipamentAPIView(ModelViewSet):
    queryset = Equipament.objects.all()
    serializer_class = EquipamentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'active']
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly, )
    
class CommentsAPIView(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['comment', 'user_id', 'equipament_id']
    permission_classes = (IsAuthenticated, )