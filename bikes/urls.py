from django.urls import path
from .views import *
from django.conf import urls

app_name = 'bikes'

urlpatterns = [
    path('', bike_list, name='bike_list'),
    path('<int:id>/', bike_detail, name='bike_detail'),
    path('bike_form/', bike_form, name='bike_form'),
    path('edit/<int:pk>/', edit_bike, name='edit'),
    path('delete/<int:pk>/', delete_bike, name='delete'),
    path(r'^$', searchposts, name='searchposts'),
    path('brand=<str:brand>/', post_by_brand, name='post_by_brand'),
    #path('ownership=<str:ownership>/', post_by_ownership, name='post_by_ownership'),
    #path('brand/', brands, name='brands'),
    path('low_to_high/', low_to_high, name='low_to_high'),
    path('high_to_low/', high_to_low, name='high_to_low'),
    path('user/<str:username>', user_vehicle_list, name='user_vehicle_list'),
    path('user1/<username>/', user_bike_list, name='user_bike_list'),
    path('user1/<username>/cars', user_bike_list, name='user_car_list'),
    path('brand', brands_new, name='brands_new'),
    path('brands/bikes', brands_new, name='brands_new_bikes'),
    path('sendEmail/',sendEmail, name="sendEmail"),
    
]