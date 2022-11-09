from rest_framework import serializers, fields
from .models import Flight, Passenger, Booking

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'
        
    def create(self, validated_data):
        return Flight.objects.create(**validated_data)
        
class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'
        
    def create(self, validated_data):
        return Passenger.objects.create(**validated_data)
        
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
        
    def create(self, validated_data):
        return Booking.objects.create(**validated_data)