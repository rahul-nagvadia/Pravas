from django.urls import path

from . import views
from pravas.views import logout_request, home_view
app_name = "bus"

urlpatterns = [
    path('search_ticket', views.search_ticket, name='search_ticket'),
    path('book_ticket', views.book_ticket, name='book_ticket'),
    path('select_seat', views.select_seat, name='select_seat'),
    path('logout', logout_request, name='logout'),
]
