from django_filters import rest_framework as filters
from .models import Product, ProductCategory
from common.filters import DisabledPaginationFilter, SearchFilter, SelectFieldsFilter

class ProductFilter(DisabledPaginationFilter, SearchFilter, SelectFieldsFilter, filters.FilterSet):
    class Meta:
        model = Product
        fields = []
    

class ProductCategoryFilter(DisabledPaginationFilter, SearchFilter, SelectFieldsFilter, filters.FilterSet):
    class Meta:
        model = ProductCategory
        fields = []
    
 