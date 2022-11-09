from rest_framework.test import APITestCase
from bookings.models import Flight, Passenger, Booking
from django.urls import reverse
from rest_framework import status

class TestViews(APITestCase):
    
    def test_flight_list_get(self):
        response = self.client.get(reverse('bookings:flight-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_passenger_list_get(self):
        response = self.client.get(reverse('bookings:passenger-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_booking_list_get(self):
        response = self.client.get(reverse('bookings:booking-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)