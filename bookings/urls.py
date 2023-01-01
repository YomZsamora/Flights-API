from django.urls import path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'flights', views.FlightViewSet, basename='flight')
router.register(r'passengers', views.PassengerViewSet, basename='passenger')
router.register(r'bookings', views.BookingViewSet, basename='booking')

urlpatterns = router.urls