from django.urls import path

from . import views

app_name = "pravas"

urlpatterns = [
    path('', views.home_view, name='home'),
    path('register', views.register_request, name='register'),
    path('login', views.login_request, name='login'),
    path('logout', views.logout_request, name='logout'),
    path('profile', views.profile_request, name='profile'),
    path('ticket_book', views.ticket_book, name='ticket_book'),
]
