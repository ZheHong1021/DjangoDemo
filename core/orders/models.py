from django.db import models
from common.models import BaseUserModel, BaseUUIDModel, RemarkModel, SoftDeleteModel
from django.db.models import Q

# Create your models here.
class Order(BaseUUIDModel, RemarkModel, SoftDeleteModel, BaseUserModel):
    PENDING = 'pending'
    PROCESSING = 'processing'
    SHIPPED = 'shipped'
    DELIVERED = 'delivered'
    CANCELLED = 'cancelled'

    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (PROCESSING, 'Processing'),
        (SHIPPED, 'Shipped'),
        (DELIVERED, 'Delivered'),
        (CANCELLED, 'Cancelled'),
    ]

    status = models.CharField("訂單狀態",
        max_length=20, 
        choices=STATUS_CHOICES, 
        default=PENDING
    )

    amount = models.IntegerField("訂單數量", blank=True, default=1)

    
    class Meta:
        db_table="orders"
