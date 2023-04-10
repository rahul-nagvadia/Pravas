from django.db import models
from pravas.models import user, City
from django.conf import settings
from django.core.exceptions import ValidationError


class Bus(models.Model):
    source = models.ForeignKey(
        City, on_delete=models.CASCADE, related_name='source')
    destination = models.ForeignKey(
        City, on_delete=models.CASCADE, related_name='destination')
    capacity = models.IntegerField()
    departure_time = models.TimeField()
    total_time = models.TimeField()
    price = models.IntegerField()

    def clean(self):
        if self.source == self.destination:
            raise ValidationError("Source and Destination can't be same")

    def __str__(self):
        return f"{self.source} - {self.destination}"

class Seat(models.Model):
    seat_number = models.IntegerField()
    
    def __str__(self):
        return f"{self.seat_number}"


class Booking(models.Model):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    date_booked = models.DateField()
    
    def __str__(self):
        return f"{self.bus} -- {self.user.username}"
