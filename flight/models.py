from django.db import models
from pravas.models import user, City
from django.conf import settings
from django.core.exceptions import ValidationError


class Flight(models.Model):
    fsource = models.ForeignKey(
        City, on_delete=models.CASCADE, related_name='fsource')
    fdestination = models.ForeignKey(
        City, on_delete=models.CASCADE, related_name='fdestination')
    capacity = models.IntegerField()
    departure_time = models.TimeField()
    total_time = models.TimeField()
    price = models.IntegerField()
    seat_class=models.CharField(max_length=20, blank=True)

    def clean(self):
        if self.fsource == self.fdestination:
            raise ValidationError("Source and Destination can't be same")


class fSeat(models.Model):
    seat_number = models.IntegerField()


class fBooking(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    seat = models.ForeignKey(fSeat, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    date_booked = models.DateField()
    seat_class=models.CharField(max_length=20, blank=True)



