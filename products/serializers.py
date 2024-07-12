from rest_framework import serializers
from .models import Product, ProductCategory
from common.serializers import ReadOnlyIdUserMixin


class ProductCategorySerializer(ReadOnlyIdUserMixin, serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = "__all__"

class ProductSerializer(ReadOnlyIdUserMixin, serializers.ModelSerializer):
    category_name = serializers.CharField(
        source="category.name",
        required=False, read_only=True
    )
    class Meta:
        model = Product
        fields = "__all__"