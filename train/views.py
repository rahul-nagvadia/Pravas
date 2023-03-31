from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from datetime import datetime

def search_view(request):
    source_station_id = request.GET["source"]
    destination_station_id = request.GET["destination"]
    date_booked = request.GET["date_booked"]
    booking_date_str = request.GET.get("date_booked")
    booking_date = datetime.strptime(booking_date_str, "%Y-%m-%d").date()
    booking_day = booking_date.strftime("%A").lower().capitalize()

    
    source_station = Station.objects.get(code=source_station_id)
    destination_station = Station.objects.get(code=destination_station_id)
    
    schedules = Schedule.objects.filter(station_id__in=[source_station_id, destination_station_id])
    schedules_by_train = {}
    for schedule in schedules:
        if schedule.train_id not in schedules_by_train:
            schedules_by_train[schedule.train_id] = []
        schedules_by_train[schedule.train_id].append(schedule)
    for train_id in schedules_by_train:
        schedules_by_train[train_id].sort(key=lambda x: x.sequence)

    trains = []
    for train_id in schedules_by_train:
        schedules = schedules_by_train[train_id]
        source_schedule = next((s for s in schedules if s.station_id == source_station_id), None)
        destination_schedule = next((s for s in schedules if s.station_id == destination_station_id), None)
        if source_schedule and destination_schedule and source_schedule.sequence < destination_schedule.sequence:
            run_days = RunDays.objects.filter(train=train_id, day=booking_day)
            if run_days.exists():
                trains.append(source_schedule.train)


    train_departure_arrival_times = {}
    for train in trains:
        schedules = schedules_by_train[train.train_number]
        source_schedule = next((s for s in schedules if s.station_id == source_station_id), None)
        destination_schedule = next((s for s in schedules if s.station_id == destination_station_id), None)
        if source_schedule and destination_schedule and source_schedule.sequence < destination_schedule.sequence:
            coach_allocations = CoachAllocation.objects.filter(train=train)
            coaches = []
            for allocation in coach_allocations:
                coaches.append(allocation.coach)
            train_departure_arrival_times[train] = {
                'departure_time': source_schedule.departure_time,
                'arrival_time': destination_schedule.arrival_time,
                'coaches': coaches,
            }

    
    context = {
        'source_station':source_station,
        'destination_station': destination_station,
        'trains': trains,
        'train_departure_arrival_times': train_departure_arrival_times,
        'date_booked':date_booked,
    }
    return render(request=request, template_name="train/search.html", context=context)


def select_view(request):
    train_id = request.GET["train_id"]
    coach_id = request.GET["coach_id"]
    date_booked = request.GET["date_booked"]
    date_booked = datetime.strptime(date_booked, '%Y-%m-%d')
    date_booked = date_booked.strftime('%d-%m-%Y')
    source = request.GET["source_name"]
    destination = request.GET["destination_name"]
    train = Train.objects.get(train_number=train_id)
    coach = Coach.objects.get(id=coach_id)
    departure_time = request.GET.get('departure_time', '')
    arrival_time = request.GET.get('arrival_time', '')
    coachAllocation=CoachAllocation.objects.get(coach=coach, train=train)
    context = {
        'train':train,
        'coach':coach,
        'coachAllocation':coachAllocation,
        'departure_time':departure_time,
        'arrival_time':arrival_time,
        'source':source,
        'destination':destination,
        'date_booked':date_booked,
    }
    return render(request=request, template_name="train/review.html", context=context)
    

def book_view(request):
    if request.method == "POST":
        date_booked = request.POST["date_booked"]
        coachAllocation = request.POST["coachAllocation_id"]
        persons = request.POST["persons"]
        
        