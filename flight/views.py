from django.shortcuts import render, redirect
from .models import Flight, fSeat, fBooking
from pravas.models import user, City
from django.contrib import messages


def search_ticket(request):
    if request.method == "POST":
        fsource = request.POST["fsource"]
        city1 = City.objects.get(city_name=fsource)
        fdestination = request.POST["fdestination"]
        city2 = City.objects.get(city_name=fdestination)
        date_booked = request.POST["date_booked"]
        flight_finded = Flight.objects.filter(fsource=city1, fdestination=city2)
        for flight in flight_finded:
            booked = 0
            bookings = fBooking.objects.filter(flight=flight, date_booked=date_booked)
            for booking in bookings:
                booked += 1
            flight.capacity = flight.capacity - booked
        context = {'flight_finded': flight_finded, 'date_booked': date_booked}
        return render(request=request, template_name="flight/search.html", context=context)


def select_seat(request):
    if request.method == "POST":
        flight_id = request.POST["flight_id"]
        flight = Flight.objects.get(id=flight_id)
        date_booked = request.POST["date_booked"]
        seat_class = request.POST["seat_class"]
        total_seats = []
        for i in range(1, flight.capacity+1):
            total_seats.append(int(i))
        bookings = fBooking.objects.filter(flight=flight, date_booked=date_booked)
        booked_seats = []
        for booking in bookings:
            booked_seats.append(booking.seat.seat_number)
        context = {'flight': flight, 'date_booked': date_booked,
                   'total_seats': total_seats, 'booked_seats': booked_seats, 'seat_class': seat_class}
        return render(request=request, template_name="flight/seat.html", context=context)


def book_ticket(request):
    if request.method == "POST":
        flight_id = request.POST["flight_id"]
        flight = Flight.objects.get(id=flight_id)
        selected = request.POST.getlist("selected")
        seat_class = request.POST["seat_class"]
        user = request.user
        date_booked = request.POST["date_booked"]
        for seat in selected:
            temp = int(seat)
            booked_seat = fSeat.objects.get(id=temp)
            obj = fBooking(flight=flight, seat=booked_seat,
                          user=user, date_booked=date_booked, seat_class=seat_class)
            obj.save()
        context = {
            'selected': selected, 'date_booked': date_booked
        }
        messages.success(request, 'Ticket is booked')
        return redirect("pravas:home")


def cancel_booking(request):
    if request.method == "POST":
        booking_id = request.POST["booking_id"]
        booking = fBooking.objects.get(id=booking_id)
        booking.delete()
        messages.success(request, 'Booking is canceled  ')
        return redirect("pravas:profile")
