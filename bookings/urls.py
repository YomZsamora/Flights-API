from django.urls import path

from . import views

app_name = 'bookings'

urlpatterns = [
    # POST: Create New Flight
    path('flight/add/', views.FlightCreateView.as_view(), name='create-flight'),
    # GET: Fetch All Flights
    path('flights/', views.FlightView.as_view(), name='flight-list'),
    # GET: Fetch All Passengers
    path('passengers/', views.PassengerView.as_view(), name='passenger-list'),
    # GET: Fetch All Bookings
    path('bookings/', views.BookingView.as_view(), name='booking-list'),
    
]