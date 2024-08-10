from rest_framework import serializers
from .models import Product, ProductCategory
from common.serializers import ReadOnlyIdUserMixin

class ProductCategorySerializer(ReadOnlyIdUserMixin, serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = "__all__"

class ProductSerializer(ReadOnlyIdUserMixin, serializers.ModelSerializer):
    # 產品名稱
    name = serializers.CharField(
        required=True,
        error_messages={
            'required': '產品名稱是必填的，請提供完整。',
            'blank': '產品名稱不能為空白，請輸入有效的名稱。',
        }
    )

    # 產品種類
    category_name = serializers.CharField(
        source="category.name",
        required=False, read_only=True
    )

    # 產品狀態文字
    status_display = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = "__all__"
    
    def get_status_display(self, instance):
        return instance.get_status_display()
