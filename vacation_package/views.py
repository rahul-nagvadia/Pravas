from django.shortcuts import render
from .models import *


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
        min_price = request.POST.get("min_price")
        max_price = request.POST.get("max_price")

        if place_id:
            packages = packages.filter(place_id=place_id)
        if month_id:
            packages = packages.filter(months__id=month_id)
        if min_price and max_price:
            packages = packages.filter(
                price__gte=min_price, price__lte=max_price)

    return render(request, 'vacation_package/package_list.html', {'packages': packages})


def package_details(request):
    if request.method == "POST":
        package_id = request.POST.get("package_id")
        package = Package.objects.get(id=package_id)

        return render(request, 'vacation_package/package.html', {'package': package})
