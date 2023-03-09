from django.urls import path

from . import views

app_name = "bus"

urlpatterns = [
    path('search_ticket', views.search_ticket, name='search_ticket'),
    path('book_ticket', views.book_ticket, name='book_ticket'),
]
