from django_filters import rest_framework as filters
from .models import Order
from common.filters import DisabledPaginationFilter, SearchFilter, SelectFieldsFilter

class OrderFilter(DisabledPaginationFilter, SearchFilter, SelectFieldsFilter, filters.FilterSet):
    class Meta:
        model = Order
        fields = []
    
