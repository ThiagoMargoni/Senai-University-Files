#biblioteca p/ trabalhar com as rotas/endpoints
from django.urls import path 

#importantdo tudo o que tem nas views
from .views import  *

urlpatterns = [
    path('people/', PeopleAPIView.as_view(), name='people'),
    path('people/<int:id>', PeopleAPIView.as_view(), name='peopleById'),
    path('planet/', PlanetAPIView.as_view(), name='planet'),
    path('planet/<int:id>', PlanetAPIView.as_view(), name='planetById'),
    path('starship/', StarshipAPIView.as_view(), name='starship'),
    path('starship/<int:id>', StarshipAPIView.as_view(), name='starshipById'),
]