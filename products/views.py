from .models import Product, ProductCategory
from .serializers import ProductSerializer, ProductCategorySerializer
from common.views import CreateWithUserMixin, UpdateWithUserMixin
from rest_framework import generics, status, viewsets
from rest_framework.permissions import IsAuthenticated # 權限
from common.paginations import CustomPagination
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiTypes, OpenApiResponse

# 建立產品種類 View
@extend_schema(
    tags=['產品種類管理'],
    request={
        'multipart/form-data': ProductCategorySerializer
    },
)
class ProductCategoryViewSet(
    CreateWithUserMixin, 
    UpdateWithUserMixin,
    viewsets.ModelViewSet
):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    permission_classes = [IsAuthenticated,]
    pagination_class = CustomPagination

# 建立產品 View
@extend_schema(
    tags=['產品管理'],
    request={
        'multipart/form-data': ProductSerializer
    },
)
class ProductViewSet(
    CreateWithUserMixin, 
    UpdateWithUserMixin,
    viewsets.ModelViewSet
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated,]
    pagination_class = CustomPagination