from django.contrib.auth.models import Group
from django.db import models
from common.models import BaseModel, BaseUUIDModel

# 自定義Group對應Django內鍵的Group
class GroupProfile(BaseUUIDModel):
    group = models.OneToOneField(Group, on_delete=models.CASCADE, related_name='profile')
    name_zh = models.CharField(max_length=100, blank=True)

    class Meta:
        db_table = "group_profile"


# MySQL View
class GroupWithProfile(models.Model):
    id = models.UUIDField(primary_key=True)  # 使用 UUIDField 作为主键
    name = models.CharField(max_length=150)
    name_zh = models.CharField(max_length=100)
    # group_id = models.IntegerField()

    class Meta:
        managed = False  # 不讓Django管理這個模型（不會創建、修改或刪除這個View）
        db_table = 'group_with_profile'  # 對應到MySQL中的View名稱