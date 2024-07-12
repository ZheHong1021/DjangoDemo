from django.db import models
from common.models import BaseUserModel, BaseUUIDModel, RemarkModel, SoftDeleteModel
from django.db.models import Q


class ProductCategory(BaseUUIDModel, SoftDeleteModel, BaseUserModel):
    name = models.CharField("產品種類", max_length=100, blank=True, unique=True)
    description = models.TextField("種類描述", blank=True, null=True)
    color = models.CharField("色塊", max_length=10, blank=True, default="#000000")
    class Meta:
        db_table="product_category"


class Product(BaseUUIDModel, SoftDeleteModel, BaseUserModel):
    AVAILABLE = 'available'
    OUT_OF_STOCK = 'out_of_stock'
    DISCONTINUED = 'discontinued'

    STATUS_CHOICES = [
        (AVAILABLE, '銷售中'),
        (OUT_OF_STOCK, '缺貨中'),
        (DISCONTINUED, '停售'),
    ]

    status = models.CharField("訂單狀態",
        max_length=20, 
        choices=STATUS_CHOICES, 
        default=OUT_OF_STOCK
    )

    name = models.CharField("產品名稱", max_length=100, blank=True, unique=True)
    description = models.TextField("產品描述", blank=True, null=True)
    price = models.IntegerField("產品價格", blank=True, default=1)
    stock = models.IntegerField("產品庫存", blank=True, default=0)
    
    category = models.ForeignKey(
        ProductCategory,
        on_delete=models.CASCADE,
        related_name='products',
        blank=True
    )

    class Meta:
        db_table="products"
