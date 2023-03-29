from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

def search_view(request):
    source_station_id = request.GET["source"]
    destination_station_id = request.GET["destination"]
    
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
            trains.append(source_schedule.train)

    train_departure_arrival_times = {}
    for train in trains:
        schedules = schedules_by_train[train.train_number]
        source_schedule = next((s for s in schedules if s.station_id == source_station_id), None)
        destination_schedule = next((s for s in schedules if s.station_id == destination_station_id), None)
        if source_schedule and destination_schedule and source_schedule.sequence < destination_schedule.sequence:
            train_departure_arrival_times[train] = {
                'departure_time': source_schedule.departure_time,
                'arrival_time': destination_schedule.arrival_time,
            }

    context = {
        'source_station':source_station,
        'destination_station': destination_station,
        'trains': trains,
        'train_departure_arrival_times': train_departure_arrival_times,
    }
    return render(request=request, template_name="train/search.html", context=context)

