from django.contrib import admin
from .models import Car, CarBrand, CarFuel, CarOwnership, CarTransmission


admin.site.register(Car)
admin.site.register(CarBrand)
admin.site.register(CarFuel)
admin.site.register(CarOwnership)
admin.site.register(CarTransmission)