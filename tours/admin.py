from django.contrib import admin
from .models import Destination, Tour, TourBooking

admin.site.register(Destination)
admin.site.register(Tour)
admin.site.register(TourBooking)
