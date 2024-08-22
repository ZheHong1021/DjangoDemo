from django.db import models
from django.contrib.auth.models import Permission


# 將 Permission 模型添加欄位 name_en
if not hasattr(Permission, 'name_zh'):
    name_zh = models.CharField(max_length=100, blank=True, null=True)
    name_zh.contribute_to_class(Permission, 'name_zh')

# # 將 Permission 模型添加欄位 
# if not hasattr(Permission, 'name_zh'):
#     name_zh = models.CharField(max_length=100, blank=True)
#     name_zh.contribute_to_class(Permission, 'name_zh')
