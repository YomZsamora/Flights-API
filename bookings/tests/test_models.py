from django.test import TestCase
from rest_framework.test import APITestCase
from bookings.models import Flight, Passenger

# Create your tests here.
class FlightModelTestCase(APITestCase):
    
    def setUp(self):
        self.test_flight = Flight.objects.create(
            from_location = 'Nairobi',
            to_location = 'Zanzibar',
            departure_time = '2022-11-10T18:00:00+03:00',
            arrival_time  = '2022-11-10T19:50:00+03:00',
            available_seats = 10
        )
    
    def test_flight_model_created_successfully(self):
        self.assertEqual(str(self.test_flight), "Flight from " + self.test_flight.from_location + " to " + self.test_flight.to_location + "!")
    
    
class PassengerModelTestCase(APITestCase):
    
    def setUp(self):
        self.test_passenger = Passenger.objects.create(
            last_name = 'Silikhe',
            first_name = 'Silas',
            email_address = 'silas.silikhe@gmail.com',
            phone_no  = '0721111061'
        )
    
    def test_passenger_model_created_successfully(self):
        self.assertEqual(str(self.test_passenger), self.test_passenger.first_name + ' ' + self.test_passenger.last_name)