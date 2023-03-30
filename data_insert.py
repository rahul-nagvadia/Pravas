import os
import django
import random
from random import randint, choice
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SPproject.settings')
django.setup()
from train.models import CoachAllocation, Coach, Train, SeatAllocation, Seat, RunDays

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

for day in days:
    # Create a new RunDays object for each day of the week
    num_trains = random.randint(6000, 10000)

    # Get a list of `num_trains` random trains
    trains = random.sample(list(Train.objects.all()), num_trains)

    # Create a new RunDays object for this day and add the trains to it
    run_day = RunDays.objects.create(day=day)
    run_day.train.set(trains)


print("Data added.")


