from .models import *
from .serializer import *
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissionsOrAnonReadOnly

from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.pagination import PageNumberPagination
import django_filters

class EquipamentAPIView(ModelViewSet):
    queryset = Equipament.objects.all()
    serializer_class = EquipamentSerializer
    filter_backends = [DjangoFilterBackend]
    pagination_class = PageNumberPagination
    filterset_fields = ['name', 'active']
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly, )

    @action(detail=False, methods=['GET'])
    def get_all(self, request):
        found = Equipament.objects.filter(create_date__year__gte=2017)
        serializer = EquipamentSerializer(found, many=True)
        return Response(serializer.data)

class CommentFilter(django_filters.FilterSet):
    comment = django_filters.CharFilter(lookup_expr='icontains')
    price = django_filters.RangeFilter()

    class Meta:
        model = Comment
        fields = ['comment', 'price']

class CommentsAPIView(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CommentFilter
    # filterset_fields = ['comment', 'price', 'user_id', 'equipament_id']
    http_method_names = ['get', 'post', 'put', 'patch']
    permission_classes = (IsAuthenticated, )

    @api_view(['GET'])
    def order_by_username(request, id):
        sorted_user = User.objects.all().order_by('username')
        found = Comment.objects.filter(equipament_id=id, user_id__in = sorted_user)
        serializer = CommentsSerializer(found, many=True)
        return Response(serializer.data)