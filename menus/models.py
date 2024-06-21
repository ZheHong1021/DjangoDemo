from django.db import models
from common.models import baseModel
import uuid

# Create your models here.
class Menu(baseModel):
    # UUID當主鍵
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    priority = models.IntegerField("顯示順位", null=True, blank=True)
    title = models.CharField("菜單名稱", max_length=50, blank=True)
    name = models.CharField("菜單路由名稱", max_length=50, blank=True)
    path = models.CharField("菜單路由路徑", max_length=50, blank=True)
    component = models.CharField("菜單路由組件", max_length=50, blank=True)
    icon = models.CharField("菜單圖案", max_length=50, blank=True)
    is_menu = models.BooleanField("是否為菜單", blank=True, default=True)
    meta = models.JSONField("前端路由設定", blank=True, null=True)
    parent = models.ForeignKey(
        'self', 
        null=True, blank=True, 
        related_name='children', 
        on_delete=models.CASCADE
    )
    
    class Meta:
        db_table="menus"
        ordering = ['priority']