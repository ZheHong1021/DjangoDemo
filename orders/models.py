from django.db import models
from utils.models import baseUserModel

# Create your models here.
class Order(baseUserModel):
    remark = models.TextField("備註", null=True, blank=True)
    
    class Meta:
        db_table="orders"