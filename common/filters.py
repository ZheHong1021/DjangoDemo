from django_filters import rest_framework as filters
from django.db.models import Q, CharField, TextField


# 透過搜尋內容篩選數據 (?no_page=)
class DisabledPaginationFilter(filters.FilterSet):
    # 不使用 Pagination
    no_page = filters.BooleanFilter(method='filter_no_page')

    class Meta:
        abstract = True

    def filter_no_page(self, queryset, name, value):
        return queryset