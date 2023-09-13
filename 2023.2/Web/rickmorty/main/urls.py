from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'location', LocationAPIView)

urlpatterns = router.urls

nameList = ['episode', 'character']
viewName = [EpisodeAPIView, CharacterAPIView]

for i in range(len(nameList)):
    urlpatterns.append(path(f'{nameList[i]}/', viewName[int(i/2)].as_view(), name=f'{nameList[i]}'))
    urlpatterns.append(path(f'{nameList[i]}/<int:id>', viewName[int(i/2)].as_view(), name=f'{nameList[i]}ById'),)