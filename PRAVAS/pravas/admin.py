from django.contrib import admin

# Register your models here.
from .models import Ticket, Tour, user, TicketBooking, TourBooking

admin.site.register(Ticket)
admin.site.register(Tour)
admin.site.register(TourBooking)
admin.site.register(TicketBooking)
admin.site.register(user)
