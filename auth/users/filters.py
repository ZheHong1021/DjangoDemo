from django_filters import rest_framework as filters
from .models import CustomUser
from common.filters import DisabledPaginationFilter, SearchFilter, SelectFieldsFilter

class UserFilter(DisabledPaginationFilter, SearchFilter, SelectFieldsFilter, filters.FilterSet):
    class Meta:
        model = CustomUser
        fields = []
    
 