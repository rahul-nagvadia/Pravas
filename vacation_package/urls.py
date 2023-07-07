from django.urls import path
from . import views

app_name = 'vacation_package'

urlpatterns = [
    path("", views.package_list, name='package_list'),
    path("package_details", views.package_details, name='package_details'),
    path("booking_template", views.booking_template, name='booking_template'),
    path("book_package", views.book_package, name='book_package'),
]
