from django.db import models

class Flight(models.Model):
    from_location = models.CharField(max_length=50)
    to_location = models.CharField(max_length=50)
    departure_time = models.DateTimeField(auto_now_add=False)
    arrival_time = models.DateTimeField(auto_now=False)
    available_seats = models.IntegerField(default=0)
    
    def __str__(self):
        return "Flight from " + self.from_location + " to " + self.to_location + "!"
    
class Passenger(models.Model):
    last_name = models.CharField(max_length=70, null=False)
    first_name = models.CharField(max_length=70, null=False)
    email_address = models.CharField(max_length=70, null=False, unique=True)
    phone_no = models.CharField(max_length=50)
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name
        

class Booking(models.Model):
    flight_id = models.ForeignKey('Flight', null=False, on_delete=models.CASCADE)
    passenger_id = models.ForeignKey('Passenger', null=False, on_delete=models.CASCADE)
    booked_seat = models.CharField(max_length=3)
    
    