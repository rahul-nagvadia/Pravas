from django.shortcuts import render, redirect
from .models import Destination, Tour, TourBooking, Comment
from pravas.models import user
from django.contrib import messages
from django.http import HttpResponse
import datetime
from django.template.loader import render_to_string

def see_tour(request, tour_id):
    tour = Tour.objects.get(id=tour_id)
    destination = tour.destinations.all()
    feedback= Comment.objects.filter(tour=tour)
    context = {'tour': tour, 'destination': destination,'feedback':feedback}
    if request.method == "POST":
        return render(request=request, template_name="tours/see_tour.html", context=context)
    else:
        return render(request=request, template_name="tours/see_tour.html", context=context)


def book_tour(request):
    if request.method == "POST":
        tour_id = request.POST["tour_id"]
        tour = Tour.objects.get(id=tour_id)
        user = request.user
        date_booked = request.POST["date_booked"]
        number_of_pass = request.POST["number_of_pass"]
        new_booking = TourBooking(
            tour=tour, user=user, date=date_booked, num_passengers=number_of_pass)
        new_booking.save()
        messages.success(request, 'Tour is booked')
        return redirect("pravas:home")

def cancel_booking(request):
    if request.method == "POST":
        booking_id = request.POST["booking_id"]
        booking = TourBooking.objects.get(id=booking_id)
        booking.delete()
        messages.success(request, 'Booking is canceled  ')
        return redirect("pravas:profile")
    
def comment_view(request):
    if request.method == "POST":
        tour_id = request.POST["tour_id"]
        tour = Tour.objects.get(id=tour_id)
        user = request.user
        comment = request.POST["comment"]
        current_datetime = datetime.datetime.now()
        feedback = Comment(user=user, tour=tour, text=comment, date=current_datetime)
        feedback.save()
        return redirect("tour:see_tour", tour_id=tour_id)
    
    