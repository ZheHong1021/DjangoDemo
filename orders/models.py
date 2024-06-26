from django.db import models
from common.models import BaseUserModel
import uuid

# Create your models here.
class Order(BaseUserModel):
    # UUID當主鍵
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    record_date = models.DateField("訂單日期", blank=True)
    remark = models.TextField("備註", null=True, blank=True)
    
    class Meta:
        db_table="orders"