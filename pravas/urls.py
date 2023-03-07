from django.urls import path
from . import views

app_name = "pravas"

urlpatterns = [
    path('', views.home_view, name='home'),
    path('register', views.register_request, name='register'),
    path('login', views.login_request, name='login'),
    path('logout', views.logout_request, name='logout'),
    # path('ticket', views.ticket_booking, name='ticket_booking'),
    path('search_ticket', views.search_ticket, name='search_ticket'),
    path('book_ticket', views.book_ticket, name='book_ticket'),
]
