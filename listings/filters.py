import django_filters
from django import forms

from .models import *

class ListingFilter(django_filters.FilterSet):
    location = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Listing

        fields = (
            "purpose",
            "property_type",
            "price",
            "num_bedrooms",
            "num_bathrooms",
            "area_size",
            "city",
            "location",
            )
        
        