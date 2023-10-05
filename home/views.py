from django.shortcuts import render
from bikes.models import Bike, Brands
from cars.models import Car, CarBrand


def index(request):
    home_bike = Bike.objects.all()[0:4]
    home_car = Car.objects.all()[0:4]
    home_brands = CarBrand.objects.all()[0:4]

    context = { 
        'home_bike': home_bike,
        'home_brands': home_brands,
        'home_car': home_car,
    }
    
    return render(request, 'index.html', context)
