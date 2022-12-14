from django.db import models
from .validators import validate_is_alpha
from django.core.validators import EmailValidator

class Flight(models.Model):
    from_location = models.CharField(max_length=50)
    to_location = models.CharField(max_length=50)
    departure_time = models.DateTimeField(auto_now_add=False)
    arrival_time = models.DateTimeField(auto_now=False)
    available_seats = models.IntegerField(default=0)
    
    def __str__(self):
        return "Flight from " + self.from_location + " to " + self.to_location + "!"
    
class Passenger(models.Model):
    last_name = models.CharField(validators=[validate_is_alpha], max_length=70, null=False)
    first_name = models.CharField(validators=[validate_is_alpha], max_length=70, null=False)
    email_address = models.EmailField(validators=[EmailValidator(message="Email does not match expected format: example@email.com")], max_length=70, null=True, unique=True, blank=False)
    phone_no = models.CharField(max_length=50)
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name
        

class Booking(models.Model):
    flight_id = models.ForeignKey('Flight', null=False, on_delete=models.CASCADE) # Many to One Relationship
    passenger_id = models.ForeignKey('Passenger', null=False, on_delete=models.CASCADE) # Many to One Relationship
    booked_seat = models.CharField(max_length=3)
    
    