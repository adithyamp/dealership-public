from django.urls import path
from .views import *

app_name = 'cars'

urlpatterns = [
    path('', car_list, name='car_list'),
    path('<int:id>', car_detail, name='car_detail'),
    path('car_form/', car_form, name='car_form'),
    path('edit/<int:pk>/', edit_car, name='edit'),
    path('delete/<int:pk>/', delete_car, name='delete'),
    path(r'^$', searchcars, name='searchcars'),
    path('brand=<str:brand>', post_by_car_brand, name='post_by_car_brand'),
    path('fuel=<str:fuel_type>', post_by_fuel, name='post_by_fuel'),
    path('transmission=<str:transmission>', post_by_transmission, name='post_by_transmission'),
    path('ownership=<str:ownership>', post_by_ownership, name='post_by_ownership'),
    path('low_to_high/', low_to_high, name='low_to_high'),
    path('high_to_low/', high_to_low, name='high_to_low'),

]