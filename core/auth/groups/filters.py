from django_filters import rest_framework as filters
from common.filters import DisabledPaginationFilter, SearchFilter, SelectFieldsFilter
from django.contrib.auth.models import Group


class GroupFilter(DisabledPaginationFilter, SearchFilter, SelectFieldsFilter, filters.FilterSet):
    class Meta:
        model = Group
        fields = []
    
 