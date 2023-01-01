from django.http import Http404
from .models import Flight, Passenger, Booking
from .serializers import FlightSerializer, PassengerSerializer, BookingSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import viewsets


# -----------------------------------------------------------
# FLIGHT VIEWS HERE
# -----------------------------------------------------------
class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    
    def get_serializer(self, *args, **kwargs):
        kwargs['partial'] = True
        return super(FlightViewSet, self).get_serializer(*args, **kwargs)



# -----------------------------------------------------------
# PASSENGER VIEWS HERE
# -----------------------------------------------------------
class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer
    
    def get_serializer(self, *args, **kwargs):
        kwargs['partial'] = True
        return super(PassengerViewSet, self).get_serializer(*args, **kwargs)



# -----------------------------------------------------------
# BOOKING VIEWS HERE
# -----------------------------------------------------------
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    
    def get_serializer(self, *args, **kwargs):
        kwargs['partial'] = True
        return super(BookingViewSet, self).get_serializer(*args, **kwargs)
    
