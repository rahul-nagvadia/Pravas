from django.shortcuts import render
from .models import Bus, Seat, Booking
from pravas.models import user, City


def search_ticket(request):
    if request.method == "POST":
        source = request.POST["source"]
        city1 = City.objects.get(city_name=source)
        destination = request.POST["destination"]
        city2 = City.objects.get(city_name=destination)
        date_booked = request.POST["date_booked"]
        bus_finded = Bus.objects.filter(source=city1, destination=city2)
        seats_data = {}
        total_seats = {}
        for bus in bus_finded:
            cap = bus.capacity
            total_seats[bus.id] = list(range(1, cap+1))
            bookings = Booking.objects.filter(bus=bus, date_booked=date_booked)
            booked_seats = []
            for booking in bookings:
                seat_n = booking.seat.seat_number
                booked_seats.append(seat_n)
            seats_data[bus.id] = booked_seats
        context = {'bus_finded': bus_finded,
                   'seats_data': seats_data, 'total_seats': total_seats, 'date_booked':date_booked}
        return render(request=request, template_name="bus/search.html", context=context)
    
def select_seat(request):
    if request.method == "POST":
        bus_id = request.POST["bus_id"]
        bus = Bus.objects.get(id=bus_id)
        date_booked = request.POST["date_booked"]

def book_ticket(request) :
    if request.method == "POST":
        bus_id = request.POST["bus_id"]
        bus = Bus.objects.get(id=bus_id)
        selected = request.POST.getlist("selected")
        user = request.user
        date_booked = request.POST["date_booked"]
        for seat in selected:
            temp = int(seat)
            booked_seat = Seat.objects.get(id=temp)
            obj = Booking(bus=bus, seat=booked_seat, user=user, date_booked=date_booked)
            obj.save()
        context = {
            'selected':selected, 'date_booked':date_booked
        }
        return render(request=request, template_name='bus/seat.html', context=context)