import django_filters
from django_filters import CharFilter, RangeFilter
from . models import *

class CarFilter(django_filters.FilterSet):
    model_name = CharFilter(field_name='model_name', lookup_expr='icontains')
    city = CharFilter(field_name='city', lookup_expr='icontains')
    kms_driven = RangeFilter(field_name='kms_driven')
    year = RangeFilter(field_name='year')
    price = RangeFilter(field_name='price')
    
    class Meta:
        model = Car
        fields = '__all__'
        exclude = ['user', 'description', 'image', 'posted', 'phone_number','brand']