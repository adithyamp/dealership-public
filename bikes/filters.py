import django_filters
from django_filters import CharFilter, RangeFilter

from .models import *

class BikeFilter(django_filters.FilterSet):
    model_name = CharFilter(field_name='model_name', lookup_expr='icontains')
    city = CharFilter(field_name='city', lookup_expr='icontains')
    price = RangeFilter(field_name='price')
    kms_driven = RangeFilter(field_name='kms_driven')
    year = RangeFilter(field_name='year')

    class Meta:
        model = Bike
        fields = '__all__'
        exclude = ['user', 'image', 'posted', 'phone_number', 'description','brand']

        