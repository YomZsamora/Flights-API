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
class BookingCreateView(APIView):
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
