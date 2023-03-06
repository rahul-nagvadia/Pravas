from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils import timezone

# Create your models here.


class user(models.Model):
    user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=200, blank=True)


class Tour(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    duration = models.PositiveSmallIntegerField(help_text='Duration in days')
    location = models.CharField(max_length=200)
    image = models.ImageField(upload_to='tour_images/')


class Ticket(models.Model):
    MODE_CHOICES = {
        ('Bus', 'Bus'),
        ('Train', 'Train'),
        ('Plane', 'Plane'),
    }
    mode = models.CharField(max_length=50, choices=MODE_CHOICES, default='Bus')
    PLACES_CHOICES = {
        ('Deesa', 'Deesa'),
        ('Nadiad', 'Nadiad'),
        ('Surat', 'Surat'),
        ('Ahmedabad', 'Ahmedabad'),
        ('Vadodara', 'Vadodara'),
        ('Jamnagar', 'Jamnagar'),
        ('Morbi', 'Morbi'),
        ('Navsari', 'Navsari'),
        ('Anand', 'Anand'),
        ('Mahesana', 'Mahesana'),
        ('Rajkot', 'Rajkot'),
    }
    source = models.CharField(
        max_length=50, choices=PLACES_CHOICES, default='Ahmedabad')
    destination = models.CharField(
        max_length=50, choices=PLACES_CHOICES, default='Ahmedabad')
    departure_time = models.TimeField()
    total_time = models.TimeField()
    OPERATORS_CHOICES = {
        ('GSRTC', 'GSRTC'),
        ('Bharat', 'Bharat'),
        ('Kabra', 'Kabra'),
        ('Tulsi', 'Tulsi'),
    }
    operators = models.CharField(
        max_length=50, choices=OPERATORS_CHOICES, default="GSRTC")

    def clean(self):
        if self.source == self.destination:
            raise ValidationError("Source and Destination can't be same")


class TourBooking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    date_booked = models.DateTimeField()
    num_adults = models.PositiveSmallIntegerField()
    num_children = models.PositiveSmallIntegerField()

    def clean(self):
        if self.date_booked < timezone.now().date():
            raise ValidationError("You cannot book ticket for past dates")


class TicketBooking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    date_booked = models.DateTimeField(auto_now=True)

    def clean(self):
        if self.date_booked < timezone.now().date():
            raise ValidationError("You cannot book ticket for past dates")