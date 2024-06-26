from django_filters import rest_framework as filters
from .models import GroupWithProfile
from common.filters import DisabledPaginationFilter, SearchFilter, SelectFieldsFilter

# 轉移出貨
class GroupFilter(DisabledPaginationFilter, SearchFilter, SelectFieldsFilter, filters.FilterSet):
    class Meta:
        model = GroupWithProfile
        fields = []
    
 