
from .views import *
from rest_framework.routers import DefaultRouter
from django.urls import path

router = DefaultRouter()
router.register(r'category',CategoryView)
router.register(r'trip',TripView)
router.register(r'image',ImageView)
router.register(r'customUser',CustomUserView)
router.register(r'booking',BookingView)
router.register(r'payment',PaymentView)
router.register(r'availability',AvailabilityView)

urlpatterns = router.urls
urlpatterns.append( path('tripScore/<int:tripId>/', ScoreAverageView.as_view(), name='trip-score-average'))
urlpatterns.append( path('conversation_history/<int:user_id>/', ConversationHistoryView.as_view(), name='conversation-history'))
urlpatterns.append( path('conversation_messages/<int:conversation_id>/', ConversationView.as_view(), name='conversation'))
urlpatterns.append( path('chatbot/', ChatBotAPIView.as_view(), name='chatbot'))