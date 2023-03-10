from django.shortcuts import render, redirect
from .models import Bus, Seat, Booking
from pravas.models import user, City
from django.contrib import messages


def search_ticket(request):
    if request.method == "POST":
        source = request.POST["source"]
        city1 = City.objects.get(city_name=source)
        destination = request.POST["destination"]
        city2 = City.objects.get(city_name=destination)
        date_booked = request.POST["date_booked"]
        bus_finded = Bus.objects.filter(source=city1, destination=city2)
        for bus in bus_finded:
            booked = 0
            bookings = Booking.objects.filter(bus=bus, date_booked=date_booked)
            for booking in bookings:
                booked += 1
            bus.capacity = bus.capacity - booked
        context = {'bus_finded': bus_finded, 'date_booked': date_booked}
        return render(request=request, template_name="bus/search.html", context=context)


def select_seat(request):
    if request.method == "POST":
        bus_id = request.POST["bus_id"]
        bus = Bus.objects.get(id=bus_id)
        date_booked = request.POST["date_booked"]
        total_seats = []
        for i in range(1, bus.capacity+1):
            total_seats.append(int(i))
        bookings = Booking.objects.filter(bus=bus, date_booked=date_booked)
        booked_seats = []
        for booking in bookings:
            booked_seats.append(booking.seat.seat_number)
        context = {'bus': bus, 'date_booked': date_booked,
                   'total_seats': total_seats, 'booked_seats': booked_seats}
        return render(request=request, template_name="bus/seat.html", context=context)


def book_ticket(request):
    if request.method == "POST":
        bus_id = request.POST["bus_id"]
        bus = Bus.objects.get(id=bus_id)
        selected = request.POST.getlist("selected")
        user = request.user
        date_booked = request.POST["date_booked"]
        for seat in selected:
            temp = int(seat)
            booked_seat = Seat.objects.get(id=temp)
            obj = Booking(bus=bus, seat=booked_seat,
                          user=user, date_booked=date_booked)
            obj.save()
        context = {
            'selected': selected, 'date_booked': date_booked
        }
        messages.success(request, 'Ticket is booked')
        return redirect("pravas:home")
