from django.contrib import admin
from .models import Destination, Tour, TourBooking, Feedback

admin.site.register(Destination)
admin.site.register(Tour)
admin.site.register(TourBooking)
admin.site.register(Feedback)
