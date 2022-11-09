from rest_framework.test import APITestCase
from bookings.models import Flight, Passenger, Booking
from django.urls import reverse
from rest_framework import status

class TestViews(APITestCase):
    
    def test_create_flight_post(self):
        flight = {
            "from_location": "Malindi",
            "to_location": "Nairobi",
            "departure_time": "2022-11-10T18:00:00+03:00",
            "arrival_time": "2022-11-10T18:45:00+03:00",
            "available_seats": 18
        }
        response = self.client.post(reverse('bookings:create-flight'), flight)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_create_flight_error(self):
        flight = {}
        response = self.client.post(reverse('bookings:create-flight'), flight)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_flight_list_get(self):
        response = self.client.get(reverse('bookings:flight-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_create_passenger_post(self):
        passenger = {
            "last_name": "Mukhanga",
            "first_name": "Bridgit",
            "email_address": "bridgit.mukhanga@gmail.com",
            "phone_no": "0702050811"
        }
        response = self.client.post(reverse('bookings:create-passenger'), passenger)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_create_passenger_error(self):
        passenger = {}
        response = self.client.post(reverse('bookings:create-passenger'), passenger)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
    def test_passenger_list_get(self):
        response = self.client.get(reverse('bookings:passenger-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_create_booking_post(self):
        test_flight = Flight.objects.create(
            from_location = "Malindi",
            to_location = "Nairobi",
            departure_time = "2022-11-10T18:00:00+03:00",
            arrival_time = "2022-11-10T18:45:00+03:00",
            available_seats = 18
        )
        test_passenger = Passenger.objects.create(
            last_name = "Mukhanga",
            first_name = "Bridgit",
            email_address = "bridgit.mukhanga@gmail.com",
            phone_no = "0702050811"
        )
        booking = {
            "booked_seat": "6B",
            "passenger_id": test_passenger.id,
            "flight_id": test_flight.id
        }
        response = self.client.post(reverse('bookings:create-booking'), booking)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_create_booking_error(self):
        booking = {}
        response = self.client.post(reverse('bookings:create-booking'), booking)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
    def test_booking_list_get(self):
        response = self.client.get(reverse('bookings:booking-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    