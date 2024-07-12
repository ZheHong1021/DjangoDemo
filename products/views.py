from .models import Product, ProductCategory
from .serializers import ProductSerializer, ProductCategorySerializer
from common.views import CreateWithUserMixin, UpdateWithUserMixin
from rest_framework import generics, status, viewsets
from rest_framework.permissions import IsAuthenticated # 權限


# 建立產品種類 View
class ProductCategoryViewSet(
    CreateWithUserMixin, 
    UpdateWithUserMixin,
    viewsets.ModelViewSet
):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    permission_classes = [IsAuthenticated,]

# 建立產品 View
class ProductViewSet(
    CreateWithUserMixin, 
    UpdateWithUserMixin,
    viewsets.ModelViewSet
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated,]