from django.db import models
from django.utils import timezone
from django.conf import settings


class Destination(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='static/tour/destinations/')


class Tour(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    destinations = models.ManyToManyField(Destination, related_name='tours')
    banner = models.ImageField(upload_to='static/tours/banners/', blank=True)


class TourBooking(models.Model):
    tour = models.ForeignKey(
        Tour, on_delete=models.CASCADE, related_name='bookings')
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='bookings')
    date = models.DateTimeField(default=timezone.now)
    num_passengers = models.PositiveIntegerField(default=1)
