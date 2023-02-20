from django.db import models

# Create your models here.


class Payment(models.Model):
    user_id = models.CharField(max_length=100)
    payment_type = models.CharField(max_length=50)
    payment_amt = models.IntegerField()
    payment_date = models.DateField()


class Booking(models.Model):
    booking_desc = models.TextField()
    booking_date = models.DateField()


class Package(models.Model):
    package_price = models.IntegerField()


class Ticket(models.Model):
    source = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    date = models.DateField()
