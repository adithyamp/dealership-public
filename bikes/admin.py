from django.contrib import admin
from . models import Bike, Brands, Ownership

admin.site.register(Bike)
admin.site.register(Brands)
admin.site.register(Ownership)