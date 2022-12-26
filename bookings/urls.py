from django.urls import path

from . import views

app_name = 'bookings'

urlpatterns = [
    # GET & POST: Create New Flight & Fetch All Flights
    path('flights/', views.FlightListAPIView.as_view(), name='flight-list'),
    # GET: /Fetched a Specific Flight Given the ID
    path('flight/<int:pk>/', views.FlightDetailView.as_view(), name='flight-details'),
    # POST: Create New Passenger
    path('passenger/add/', views.PassengerCreateView.as_view(), name='create-passenger'),
    # GET: Fetch All Passengers
    path('passengers/', views.PassengerListView.as_view(), name='passenger-list'),
    # GET: /Fetched a Specific Passenger Given the ID
    path('passenger/<int:pk>/', views.PassengerDetailView.as_view(), name='passenger-details'),
    # POST: Create New Booking
    path('booking/add/', views.BookingCreateView.as_view(), name='create-booking'),
    # GET: Fetch All Bookings
    path('bookings/', views.BookingListView.as_view(), name='booking-list'),
    # GET: /Fetched a Specific Booking Given the ID
    path('booking/<int:pk>/', views.BookingDetailView.as_view(), name='booking-details'),
    
]