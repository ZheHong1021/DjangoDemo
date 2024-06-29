from django.db import models
from users.models import CustomUser

# 用戶的外來鍵
class BaseUserForeignKey(models.ForeignKey):
    def __init__(self, to, **kwargs):
        kwargs['db_column'] = 'user_id'
        super().__init__(to, **kwargs)


# 一般資訊(無用戶)
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta: 
        abstract = True

# 一般資訊(有用戶)
class BaseUserModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = BaseUserForeignKey(
        CustomUser, 
        on_delete=models.CASCADE,
        blank=True, # 允許不修改
    )

    class Meta: 
        abstract = True


# UUID作為主鍵
import uuid
class BaseUUIDModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    class Meta: 
        abstract = True



# 軟刪除
class SoftDeleteModel(models.Model):
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True

    def delete(self, *args, **kwargs):
        self.is_deleted = True
        self.save()
