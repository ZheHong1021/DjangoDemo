from common.filters import DisabledPaginationFilter, IDsFilter, SearchFilter

class PermissionFilter(DisabledPaginationFilter, IDsFilter, SearchFilter):
    class Meta:
        fields = ['no_page', 'ids', 'search']