from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError


class Station(models.Model):
    code = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.code}"


class Train(models.Model):
    train_number = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.train_number}"


class Seat(models.Model):
    seat_number = models.IntegerField(primary_key=True)

    def __str__(self):
        return f"{self.seat_number}"


class Coach(models.Model):
    id = models.IntegerField(primary_key=True)
    COACH_TYPE = (
        ("EC", "EC"),
        ("1AC", "1AC"),
        ("2AC", "2AC"),
        ("3AC", "3AC"),
        ("FC", "FC"),
        ("CC", "CC"),
        ("SL", "SL"),
        ("2S", "2S"),
    )
    capacity = models.IntegerField()
    type = models.CharField(max_length=10, choices=COACH_TYPE, default="2S")
    prize = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.type} - {self.capacity}"


class CoachAllocation(models.Model):
    id = models.IntegerField(primary_key=True)
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE)
    train = models.ForeignKey(Train, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.train} - {self.coach}"


class SeatAllocation(models.Model):
    id = models.IntegerField(primary_key=True)
    coachAllocation = models.ForeignKey(
        CoachAllocation, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.coachAllocation} - {self.seat}"


class RunDays(models.Model):
    day = models.CharField(primary_key=True, max_length=10)
    train = models.ManyToManyField(Train)

    def __str__(self):
        return f"{self.day}"


class Schedule(models.Model):
    id = models.IntegerField(primary_key=True)
    sequence = models.PositiveIntegerField()
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    arrival_time = models.TimeField()
    departure_time = models.TimeField()
    distance = models.IntegerField()


class TrainBooking(models.Model):
    train_schedule = models.ForeignKey(
        Train, on_delete=models.CASCADE)
    seat_allocation = models.ForeignKey(
        SeatAllocation, on_delete=models.CASCADE)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL,
    #                          on_delete=models.CASCADE)
    date_booked = models.DateField()

    def __str__(self):
        return f'{self.train_schedule.train} - Seat {self.seat_allocation.seat.seat_number} ({self.date_booked})'
