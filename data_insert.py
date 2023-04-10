import os
import django
import random
from random import randint, choice
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SPproject.settings')
django.setup()
from train.models import CoachAllocation, Coach, Train, SeatAllocation, Seat, RunDays

i = 15539
coach_allocations = CoachAllocation.objects.filter(id__gt=15538) 
for coach_allocation in coach_allocations:
    # Get the coach and its capacity
    coach = coach_allocation.coach
    capacity = coach.capacity

    seat_allocation = SeatAllocation.objects.create(id=i, coachAllocation=coach_allocation)

    # Create seats for this coach allocation
    for seat_number in range(1, capacity + 1):
        seat, created = Seat.objects.get_or_create(seat_number=seat_number)
        seat_allocation.seat.add(seat)

    i += 1

print("Data added to SeatAllocation model.")
