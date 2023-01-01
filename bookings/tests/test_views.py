from rest_framework.test import APITestCase
from bookings.models import Flight, Passenger, Booking
from django.urls import reverse
from rest_framework import status
from bookings.serializers import FlightSerializer, PassengerSerializer, BookingSerializer

class TestViews(APITestCase):
    
    def setUp(self):
        Flight.objects.bulk_create([
            Flight(from_location = "Malindi", to_location = "Nairobi", departure_time = "2022-11-10T18:00:00+03:00", arrival_time = "2022-11-10T18:45:00+03:00", available_seats = 18),
            Flight(from_location = "Eldoret", to_location = "Kisumu", departure_time = "2022-12-04T18:00:00+03:00", arrival_time = "2023-01-08T11:45:00+03:00", available_seats = 22),
        ])
        
        Passenger.objects.bulk_create([
            Passenger(last_name = "Mukhanga", first_name = "Bridgit", email_address = "bridgit.mukhanga@gmail.com", phone_no = "0702050811"),
            Passenger(last_name = "Busolo", first_name = "Wendy", email_address = "wendy.busolo@gmail.com", phone_no = "0110987123"),
            Passenger(last_name = "Muli", first_name = "Timothy", email_address = "timothy.muli@gmail.com", phone_no = "0712345987"),
        ])
        
        test_flight = Flight.objects.get(pk=1)
        test_passenger = Passenger.objects.get(pk=2)
        booking = {
            "booked_seat": "6B",
            "passenger": test_passenger.id,
            "flight": test_flight.id
        }
        self.client.post(reverse('bookings:create-booking'), booking)
        
    
    # -----------------------------------------------------------
    # FLIGHT TESTS HERE
    # -----------------------------------------------------------
    def test_create_flight_POST(self):
        flight = Flight.objects.get(pk=1)
        serializer = FlightSerializer(flight)
        response = self.client.post(reverse('bookings:flight-list'), serializer.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_create_flight_error(self):
        flight = {}
        response = self.client.post(reverse('bookings:flight-list'), flight)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_flight_list_GET(self):
        response = self.client.get(reverse('bookings:flight-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data)
        
    def test_flight_details_GET(self):
        response = self.client.get(reverse('bookings:flight-details', kwargs={"pk": 2}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['available_seats'], 22)
        
    def test_flight_does_not_exist_GET(self):
        response = self.client.get(reverse('bookings:flight-details', kwargs={"pk": 4}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
    def test_flight_details_update_PUT(self):
        response = self.client.put(reverse('bookings:flight-details', kwargs={"pk": 2}), {'available_seats': 6})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['available_seats'], 6)
        
    def test_flight_details_update_error(self):
        invalid_post = {
            "available_seats": "12", # Should be Number of IntegerField
            "departure_time": "11/02/2022" # Invalid DateTimeField Format
        }
        response = self.client.put(reverse('bookings:flight-details', kwargs={"pk": 1}), invalid_post) 
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
    def test_flight_details_DELETE(self):
        response = self.client.delete(reverse('bookings:flight-details', kwargs={"pk": 2}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Flight.objects.count(), 1)
        
        
    
    # -----------------------------------------------------------
    # PASSENGER TESTS HERE
    # -----------------------------------------------------------    
    def test_create_passenger_POST(self):
        passenger = { # Add a New Passenger Object to the list of Passenger Objects
            "last_name": "Stevo",
            "first_name": "BigMan",
            "email_address": "bigman.stevo@comrades.com",
            "phone_no": "0112345096"
        }
        response = self.client.post(reverse('bookings:passenger-list'), passenger)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Passenger.objects.count(), 4)
        self.assertEqual(Passenger.objects.get(pk=4).email_address, "bigman.stevo@comrades.com")
        
    def test_create_passenger_error(self):
        passenger = {}
        response = self.client.post(reverse('bookings:passenger-list'), passenger)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
    def test_passenger_list_GET(self):
        response = self.client.get(reverse('bookings:passenger-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data)
        
    def test_passenger_details_GET(self):
        response = self.client.get(reverse('bookings:passenger-details', kwargs={'pk': 3}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email_address'], "timothy.muli@gmail.com")
        
    def test_passenger_does_not_exist_GET(self):
        response = self.client.get(reverse('bookings:passenger-details', kwargs={'pk': 4}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
    def test_passenger_details_update_PUT(self):
        response = self.client.put(reverse('bookings:passenger-details', kwargs={"pk": 2}), {'email_address': "w.bus@adzumi.co.ke"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email_address'], "w.bus@adzumi.co.ke")
        
    def test_passenger_details_update_error(self):
        invalid_post = {
            "last_name": "Muthomi9", # Name Should Not Contain a Number
        }
        response = self.client.put(reverse('bookings:passenger-details', kwargs={"pk": 1}), invalid_post) 
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
    def test_passenger_details_DELETE(self):
        response = self.client.delete(reverse('bookings:passenger-details', kwargs={'pk': 3}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Passenger.objects.count(), 2)
    
    
    
    # -----------------------------------------------------------
    # BOOKING TESTS HERE
    # -----------------------------------------------------------
    def test_create_booking_POST(self):
        test_flight = Flight.objects.get(pk=1)
        test_passenger = Passenger.objects.get(pk=2)
        booking = {
            "booked_seat": "6B",
            "passenger": test_passenger.id,
            "flight": test_flight.id
        }
        response = self.client.post(reverse('bookings:create-booking'), booking)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_create_booking_error(self):
        booking = {}
        response = self.client.post(reverse('bookings:create-booking'), booking)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
    def test_booking_list_GET(self):
        response = self.client.get(reverse('bookings:booking-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data)
        
    def test_booking_details_GET(self):
        response = self.client.get(reverse('bookings:booking-details', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['booked_seat'], "6B")
        
    def test_booking_does_not_exist_GET(self):
        response = self.client.get(reverse('bookings:booking-details', kwargs={'pk': 3}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
    def test_booking_details_update_PUT(self):
        response = self.client.put(reverse('bookings:booking-details', kwargs={"pk": 1}), {'booked_seat': "19A"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['booking']['booked_seat'], "19A")
        
    def test_booking_details_update_error(self):
        invalid_post = {
            "passenger": 27, # Passenger With ID 27 Doesn't Exist
        }
        response = self.client.put(reverse('bookings:booking-details', kwargs={"pk": 1}), invalid_post) 
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
    def test_booking_details_DELETE(self):
        response = self.client.delete(reverse('bookings:booking-details', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Booking.objects.count(), 0)
        
    