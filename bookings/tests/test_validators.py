
from rest_framework.test import APITestCase
from bookings.models import Passenger
from django.core.validators import ValidationError

class TestValidators(APITestCase):
    
    def test_isaplha_for_passenger_names(self):
        # Test that first_name and last_name are not containing any digits
        test_passenger = Passenger(
            last_name = 'Kimutai',
            first_name = 'Kiprotich34',
            email_address = 'kiprotich.kim@gmail.com',
            phone_no  = '0721111061'
        )
        with self.assertRaises(ValidationError):
            test_passenger.full_clean()