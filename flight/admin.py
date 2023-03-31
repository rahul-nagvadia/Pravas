from django.contrib import admin
from .models import Flight, fSeat, fBooking


admin.site.register(Flight)
admin.site.register(fSeat)
admin.site.register(fBooking)

