from django.urls import path
from . import views

app_name = 'vacation_package'

urlpatterns = [
    path('packages/', views.package_list, name='package_list'),
    path('packages/by_destination/', views.package_list_by_destination,
         name='package_list_by_destination'),
    path('packages/by_theme/', views.package_list_by_theme,
         name='package_list_by_theme'),
    path('packages/by_month/', views.package_list_by_month,
         name='package_list_by_month'),
    path('packages/by_price/', views.package_list_by_price,
         name='package_list_by_price'),
    path('packages/by_multiple_choices/', views.package_list_by_multiple_choices,
         name='package_list_by_multiple_choices'),
]
