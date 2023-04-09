from django.urls import path

from . import views

app_name = "tour"

urlpatterns = [
    path('see_tour/<int:tour_id>', views.see_tour, name='see_tour'),
    path('book_tour', views.book_tour, name='book_tour'),
    path('cancel_booking', views.cancel_booking, name='cancel_booking'),     
    path('comment_view', views.comment_view, name='comment_view'), 
]
