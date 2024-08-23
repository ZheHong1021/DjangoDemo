from django.contrib.auth.models import Group
from django.db import models
from common.models import BaseUUIDModel, SoftDeleteModel
from django.db.models import Q

class GroupProfile(BaseUUIDModel, SoftDeleteModel):
    group = models.OneToOneField(Group, on_delete=models.CASCADE, related_name='profile')
    name_zh = models.CharField(max_length=100, blank=True, unique=True)

    class Meta:
        db_table = "group_profile"

        constraints = [
            models.UniqueConstraint(
                fields=['name_zh', 'group', 'deleted_at'], 
                name='unique_group_name_deleted_at'
            )
        ]
    
    


# MySQL View
class GroupWithProfile(models.Model):
    id = models.UUIDField(primary_key=True)  # 使用 UUIDField 作为主键
    name = models.CharField(max_length=150)
    name_zh = models.CharField(max_length=100)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        managed = False  # 不讓Django管理這個模型（不會創建、修改或刪除這個View）
        db_table = 'group_with_profile'  # 對應到MySQL中的View名稱