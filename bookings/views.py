from django.shortcuts import render
from .models import Flight, Passenger, Booking
from .serializers import FlightSerializer, PassengerSerializer, BookingSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class FlightCreateView(APIView):
    def post(self, request):
        serializer = FlightSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'data': serializer.data }, status=status.HTTP_201_CREATED)
        else:
            return Response({ 'data': serializer.errors }, status=status.HTTP_400_BAD_REQUEST)

class FlightView(APIView):
    def get(self, request):
        flights = Flight.objects.all()
        serializer = FlightSerializer(flights, many=True)
        return Response({ 'Flights': serializer.data }, status=status.HTTP_200_OK)

class PassengerView(APIView):
    def get(self, request):
        passengers = Passenger.objects.all()
        serializer = PassengerSerializer(passengers, many=True)
        return Response({ 'Passengers': serializer.data }, status=status.HTTP_200_OK)
    
class BookingView(APIView):
    def get(self, request):
        bookings = Booking.objects.all()
        serializer = BookingSerializer(bookings, many=True)
        return Response({ 'Bookings': serializer.data }, status=status.HTTP_200_OK)
        

