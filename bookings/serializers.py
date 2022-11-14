from rest_framework import serializers, fields
from .models import Flight, Passenger, Booking

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'
        
    def create(self, validated_data):
        return Flight.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.from_location = validated_data.get('from_location', instance.from_location)
        instance.to_location = validated_data.get('to_location', instance.to_location)
        instance.departure_time = validated_data.get('departure_time', instance.departure_time)
        instance.arrival_time = validated_data.get('arrival_time', instance.arrival_time)
        instance.available_seats = validated_data.get('available_seats', instance.available_seats)
        instance.save()
        return instance
        
class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'
        
    def create(self, validated_data):
        return Passenger.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.email_address = validated_data.get('email_address', instance.email_address)
        instance.phone_no = validated_data.get('phone_no', instance.phone_no)
        instance.save()
        return instance
        
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
        
    def create(self, validated_data):
        return Booking.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.flight_id = validated_data.get('flight_id', instance.flight_id)
        instance.passenger_id = validated_data.get('passenger_id', instance.passenger_id)
        instance.booked_seat = validated_data.get('booked_seat', instance.booked_seat)
        instance.save()
        return instance