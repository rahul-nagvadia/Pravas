from django.shortcuts import render
from .models import *


def package_list(request):
    packages = Package.objects.all()
    return render(request, "vacation_package/package_list.html", {"packages": packages})


def package_list_by_destination(request):
    place_id = request.GET.get("place_id")
    place = Place.objects.get(id=place_id)
    packages = Package.objects.filter(place=place)
    return render(request, "vacation_package/package_list.html", {"packages": packages})


def package_list_by_theme(request):
    theme_id = request.GET.get("theme_id")
    theme = Theme.objects.get(id=theme_id)
    packages = Package.objects.filter(themes__in=[theme])
    return render(request, "vacation_package/package_list.html", {"packages": packages})


def package_list_by_month(request):
    month_id = request.GET.get("month_id")
    month = Month.objects.get(id=month_id)
    packages = month.packages.all()
    return render(request, 'vacation_package/package_list.html', {'packages': packages})


def package_list_by_price(request):
    min_price = request.GET.get("min_price")
    max_price = request.GET.get("max_price")
    packages = Package.objects.filter(
        price__gte=min_price, price__lte=max_price)

    return render(request, 'vacation_package/package_list.html', {'packages': packages})


def package_list_by_multiple_choices(request):
    if request.method == "POST":
        place_id = request.POST.get("place_id")
        month_id = request.POST.get("month_id")
        min_price = request.POST.get("min_price")
        max_price = request.POST.get("max_price")

        packages = Package.objects.all()

        if place_id:
            packages = packages.filter(place_id=place_id)
        if month_id:
            packages = packages.filter(months__id=month_id)
        if min_price and max_price:
            packages = packages.filter(
                price__gte=min_price, price__lte=max_price)

    return render(request, 'vacation_package/package_list.html', {'packages': packages})
