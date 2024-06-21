from django_filters import rest_framework as filters
from .models import Menu

# 轉移出貨
class MenuFilter(filters.FilterSet):
    # 被轉移的案場ID
    is_children = filters.BooleanFilter(
        method='filter_is_children'
    )

    class Meta:
        model = Menu
        fields = [
            'is_children', 
        ]
    
    def filter_is_children(self, queryset, name, value):
        if value:
            return queryset.filter(parent__isnull=False)
        return queryset.filter(parent__isnull=True)