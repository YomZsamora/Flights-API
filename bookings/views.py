from django.http import Http404
from .models import Flight, Passenger, Booking
from .serializers import FlightSerializer, PassengerSerializer, BookingSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# -----------------------------------------------------------
# FLIGHT VIEWS HERE
# -----------------------------------------------------------
class FlightCreateView(APIView):
    def post(self, request):
        serializer = FlightSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'data': serializer.data }, status=status.HTTP_201_CREATED)
        else:
            return Response({ 'data': serializer.errors }, status=status.HTTP_400_BAD_REQUEST)

class FlightListView(APIView):
    def get(self, request):
        flights = Flight.objects.all()
        serializer = FlightSerializer(flights, many=True)
        return Response({ 'Flights': serializer.data }, status=status.HTTP_200_OK)
    
class FlightDetailView(APIView):
    def get_flight_by_pk(self, pk):
        try:
            return Flight.objects.get(pk=pk)
        except:
            raise Http404
        
    def get(self, request, pk):
        flight = self.get_flight_by_pk(pk)
        serializer = FlightSerializer(flight)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        flight = self.get_flight_by_pk(pk)
        serializer = FlightSerializer(flight, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"flight": serializer.data, "message": "Flight Updated Successfully!"}, status=status.HTTP_200_OK)
        return Response({"data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        flight = self.get_flight_by_pk(pk)
        flight.delete()
        return Response({"messages": "Selected Flight Has Beed Deleted!"}, status=status.HTTP_204_NO_CONTENT)


# -----------------------------------------------------------
# PASSENGER VIEWS HERE
# -----------------------------------------------------------
class PassengerCreateView(APIView):
    def post(self, request):
        serializer = PassengerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'data': serializer.data }, status=status.HTTP_201_CREATED)
        else:
            return Response({ 'data': serializer.errors }, status=status.HTTP_400_BAD_REQUEST)

class PassengerListView(APIView):
    def get(self, request):
        passengers = Passenger.objects.all()
        serializer = PassengerSerializer(passengers, many=True)
        return Response({ 'Passengers': serializer.data }, status=status.HTTP_200_OK)
    
class PassengerDetailView(APIView):
    def get_passenger_by_pk(self, pk):
        try:
            return Passenger.objects.get(pk=pk)
        except:
            raise Http404
        
    def get(self, request, pk):
        passenger = self.get_passenger_by_pk(pk)
        serializer = PassengerSerializer(passenger)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        passenger = self.get_passenger_by_pk(pk)
        serializer = PassengerSerializer(passenger, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"passenger": serializer.data, "message": "Passenger Updated Successfully!"}, status=status.HTTP_200_OK)
        return Response({"data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        passenger = self.get_passenger_by_pk(pk)
        passenger.delete()
        return Response({"messages": "Selected Passenger Has Beed Deleted!"}, status=status.HTTP_204_NO_CONTENT)


# -----------------------------------------------------------
# BOOKING VIEWS HERE
# -----------------------------------------------------------
    def post(self, request):
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'data': serializer.data }, status=status.HTTP_201_CREATED)
        else:
            return Response({ 'data': serializer.errors }, status=status.HTTP_400_BAD_REQUEST)
    
class BookingListView(APIView):
    def get(self, request):
        bookings = Booking.objects.all()
        serializer = BookingSerializer(bookings, many=True)
        return Response({ 'Bookings': serializer.data }, status=status.HTTP_200_OK)
        
class BookingDetailView(APIView):
    def get_booking_by_pk(self, pk):
        try:
            return Booking.objects.get(pk=pk)
        except:
            raise Http404
        
    def get(self, request, pk):
        booking = self.get_booking_by_pk(pk)
        serializer = BookingSerializer(booking)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        booking = self.get_booking_by_pk(pk)
        serializer = BookingSerializer(booking, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"booking": serializer.data, "message": "Booking Updated Successfully!"}, status=status.HTTP_200_OK)
        return Response({"data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        booking = self.get_booking_by_pk(pk)
        booking.delete()
        return Response({"messages": "Selected Booking Has Beed Deleted!"}, status=status.HTTP_204_NO_CONTENT)
