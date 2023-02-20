from django.contrib import admin

# Register your models here.
from .models import Ticket, Package, Payment, Booking

admin.site.register(Ticket)
admin.site.register(Package)
admin.site.register(Payment)
admin.site.register(Booking)
