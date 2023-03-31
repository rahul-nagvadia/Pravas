from django.contrib import admin
from .models import *

admin.site.register(Station)
admin.site.register(Train)
admin.site.register(Seat)
admin.site.register(Coach)
admin.site.register(CoachAllocation)
admin.site.register(SeatAllocation)
admin.site.register(RunDays)
admin.site.register(Schedule)
admin.site.register(TrainBooking)
