from django.urls import path

from . import views
app_name = "train"

urlpatterns = [
    path('search', views.search_view),
    path('select', views.select_view),
    path('book', views.book_view),
]
