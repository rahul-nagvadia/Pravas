from django.shortcuts import render, redirect
from .models import *
from datetime import datetime, timedelta
from administration.views import home_view


def package_list_by_theme(request):
    theme_id = request.GET.get("theme_id")
    theme = Theme.objects.get(id=theme_id)
    packages = Package.objects.filter(themes__in=[theme])
    return render(request, "vacation_package/package_list.html", {"packages": packages})


def package_list(request):
    packages = Package.objects.all()
    if request.method == "POST":
        place_id = request.POST.get("place_id")
        month_id = request.POST.get("month_id")
        selected_month = Month.objects.get(id=month_id)
        max_price = request.POST.get("max_price")
        packages = selected_month.packages
        if place_id:
            packages = packages.filter(place_id=place_id)
        if max_price:
            packages = packages.filter(price__lte=max_price)
    return render(request, 'vacation_package/package_list.html', {'packages': packages, 'month_id': month_id})


def package_details(request):
    if request.method == "POST":
        month_id = request.POST.get("month_id")
        package_id = request.POST.get("package_id")
        package = Package.objects.get(id=package_id)
        return render(request, 'vacation_package/package.html', {'package': package, 'month_id': month_id})


def booking_template(request):
    if request.method == "POST":
        month_id = request.POST.get("month_id")
        selected_month = Month.objects.get(id=month_id)
        package_id = request.POST.get("package_id")
        package = Package.objects.get(id=package_id)
        return render(request, 'vacation_package/booking.html', {'package': package, 'month': selected_month})


def book_package(request):
    months = {
        "January": 0,
        "February": 1,
        "March": 2,
        "April": 3,
        "May": 4,
        "June": 5,
        "July": 6,
        "August": 7,
        "September": 8,
        "October": 9,
        "November": 10,
        "December": 11
    }

    if request.method == "POST":
        package_id = request.POST.get('package_id')
        children = int(request.POST.get('children'))
        adults = int(request.POST.get('adults'))
        selected_day = int(request.POST.get('selected_day'))
        package = Package.objects.get(id=package_id)
        user = request.user
        selected_month = request.POST.get('month_id')

        current_datetime = datetime.now()
        selected_date = datetime(
            current_datetime.year, int(selected_month), selected_day)

        if selected_date < current_datetime:
            year = current_datetime.year + 1
        else:
            year = current_datetime.year

        booking_date = datetime(year, int(selected_month), selected_day).date()

        booking = Package_Booking.objects.create(
            package=package,
            user=user,
            children=children,
            Adult=adults,
            date_booked=booking_date
        )

        return redirect('administration:home')
    else:
        return render(request, 'booking_form.html')
