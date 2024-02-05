from django.urls import path
from .views import *

urlpatterns = [
    path('chatbot/', ChatBotView.as_view(), name='chatbot'),
]