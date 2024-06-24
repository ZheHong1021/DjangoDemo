from django.db import models
from common.models import BaseModel
import uuid

# Create your models here.
class Menu(BaseModel):
    # UUID當主鍵
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    priority = models.IntegerField("顯示順位", null=True, blank=True)
    title = models.CharField("菜單名稱", max_length=50, blank=True)
    name = models.CharField("菜單路由名稱", max_length=50, blank=True, unique=True, default='name')
    path = models.CharField("菜單路由路徑", max_length=50, blank=True, unique=True, default='path')
    component = models.CharField("菜單路由組件", max_length=50, blank=True, unique=True, default='component')
    redirect = models.CharField("跳轉路徑", max_length=50, blank=True, null=True)
    icon = models.CharField("菜單圖案", max_length=50, blank=True, null=True)
    is_menu = models.BooleanField("是否為菜單", blank=True, default=True)
    is_disabled = models.BooleanField("是否停用", blank=True, default=False)
    parent = models.ForeignKey(
        'self', 
        null=True, blank=True, 
        related_name='children', 
        on_delete=models.CASCADE
    )
    
    class Meta:
        db_table="menus"
        ordering = ['priority']