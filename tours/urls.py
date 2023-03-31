from django.urls import path

from . import views

app_name = "tour"

urlpatterns = [
    path('see_tour', views.see_tour, name='see_tour'),
    path('book_tour', views.book_tour, name='book_tour'),
    path('comment',views.comment, name='comment'),
    path('cancel_booking', views.cancel_booking, name='cancel_booking'),        
]
