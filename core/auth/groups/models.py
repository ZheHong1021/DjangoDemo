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
    
    

