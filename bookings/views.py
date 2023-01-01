from django.http import Http404
from .models import Flight, Passenger, Booking
from .serializers import FlightSerializer, PassengerSerializer, BookingSerializer
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status

# -----------------------------------------------------------
# FLIGHT VIEWS HERE
# -----------------------------------------------------------
class FlightListAPIView(ListCreateAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    
class FlightDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    
    # Implements Partial Update
    def get_serializer(self, *args, **kwargs):
        kwargs['partial'] = True
        return super(FlightDetailAPIView, self).get_serializer(*args, **kwargs)



# -----------------------------------------------------------
# PASSENGER VIEWS HERE
# -----------------------------------------------------------
class PassengerListAPIView(ListCreateAPIView):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer
    
class PassengerDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer
    
    #Implement Partial Update
    def get_serializer(self, *args, **kwargs):
        kwargs['partial'] = True
        return super(PassengerDetailAPIView, self).get_serializer(*args, **kwargs)



# -----------------------------------------------------------
# BOOKING VIEWS HERE
# -----------------------------------------------------------
class BookingListAPIVIew(ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer 
    
class BookingDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    
    # Implement Partial Update
    def get_serializer(self, *args, **kwargs):
        kwargs['partial'] = True
        return super(BookingDetailAPIView, self).get_serializer(*args, **kwargs)
    
