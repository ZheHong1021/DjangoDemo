from django.db import models
from users.models import CustomUser

# 用戶的外來鍵
class BaseUserForeignKey(models.ForeignKey):
    def __init__(self, to, **kwargs):
        kwargs['db_column'] = 'user_id'
        super().__init__(to, **kwargs)


# 一般資訊(無用戶)
class baseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta: 
        abstract = True

# 一般資訊(有用戶)
class baseUserModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = BaseUserForeignKey(
        CustomUser, 
        on_delete=models.CASCADE
    )

    class Meta: 
        abstract = True