from rest_framework import serializers
from .models import Product, ProductCategory
from common.serializers import ReadOnlyIdUserMixin
from rest_framework.validators import UniqueValidator

class ProductCategorySerializer(ReadOnlyIdUserMixin, serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = "__all__"

class ProductSerializer(ReadOnlyIdUserMixin, serializers.ModelSerializer):
    # 產品名稱
    name = serializers.CharField(
        help_text="請輸入字元長度2~12且不重複的產品名稱。",
        required=True,
        min_length=2,
        max_length=12,
        error_messages={
            'required': '產品名稱是必填的，請提供完整。',
        },
        validators=[
            UniqueValidator( # 唯一性錯誤回傳
                queryset=Product.objects.all(), 
                message="該產品名稱已經被使用，請使用其他名稱!。"
            )
        ]
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
