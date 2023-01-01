from django.urls import path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'flights', views.FlightViewSet)

urlpatterns = router.urls


# urlpatterns = [
#     # GET & POST: Create New Flight & Fetch All Flights
#     path('flights/', views.FlightListAPIView.as_view(), name='flight-list'),
#     # GET, PUT & DELETE: /Fetched a Specific Flight Given the ID
#     path('flight/<int:pk>/', views.FlightDetailAPIView.as_view(), name='flight-details'),
#     # GET & POST: Create New Passenger & Fetch All Passengers
#     path('passengers/', views.PassengerListAPIView.as_view(), name='passenger-list'),
#     # GET: /Fetched a Specific Passenger Given the ID
#     path('passenger/<int:pk>/', views.PassengerDetailAPIView.as_view(), name='passenger-details'),
#     # GET & POST: Create New Booking & Fetch All Bookings
#     path('bookings/', views.BookingListAPIVIew.as_view(), name='booking-list'),
#     # GET: /Fetched a Specific Booking Given the ID
#     path('booking/<int:pk>/', views.BookingDetailAPIView.as_view(), name='booking-details'),
    
# ]