from rest_framework import serializers
from django.contrib.auth.models import Group, Permission
from .models import GroupProfile, GroupWithProfile
from permissions.serializers import PermissionSerializer
from django.db import transaction

# Profile
class GroupProfileSerializer(serializers.ModelSerializer):
    name = serializers.CharField( # Group Name
        source='group.name'
    )
    name_zh = serializers.CharField( # Group Name in Chinese
        required=True
    )

    # 權限
    permissions = serializers.CharField(
        required=False, allow_blank=True
    )


    class Meta:
        model = GroupProfile
        fields = ['id', 'name', 'name_zh', 'permissions', 'group_id']
    
    # 如果还需要通过GET方法获取权限数据
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['permissions'] = PermissionSerializer(instance.group.permissions.all(), many=True).data
        return representation
    
    
    # 驗證該 Group有存在
    def validate_name(self, value):
        if self.instance and self.instance.group.name == value:
            return value
        
        if Group.objects.filter(name__exact=value).exists():
            raise serializers.ValidationError("該角色代號已經存在!")
        return value
    
    def validate_name_zh(self, value):
        if self.instance and self.instance.name_zh == value:
            return value
        if GroupProfile.objects.filter(name_zh__exact=value).exists():
            raise serializers.ValidationError("該角色名稱已經存在!")
        return value

    # 創建
    @transaction.atomic # 確認都正確才執行操作
    def create(self, validated_data):
        group_data = validated_data.pop('group') # 取出 Group Data
        permissions_data = validated_data.pop('permissions', None) # 取出 Group Data


        group = Group.objects.create(**group_data) # 創建 Group
        group_profile = GroupProfile.objects.create( # 創建 Group Profile
            group=group, 
            **validated_data
        )

        # 權限
        if permissions_data:
            permissions_data = permissions_data.split(',') # 轉換成 List
            group_profile.group.permissions.add(*permissions_data) # 添加權限
           
        return group_profile

    @transaction.atomic # 確認都正確才執行操作
    def update(self, instance, validated_data):
        group_data = validated_data.pop('group', None) # 取出 Group Data
        permissions_data = validated_data.pop('permissions', None) # 取出 Group Data

        if group_data: # 如果有 Group Data
            group = instance.group
            group.name = instance.group.name
            group.save() # 更新 Group
        
        # 權限
        if permissions_data is not None:
            instance.group.permissions.clear() # 清空權限
            if permissions_data:
                permissions_data = permissions_data.split(',') # 轉換成 List
                instance.group.permissions.add(*permissions_data) # 添加權限

        return super().update(instance, validated_data)


# MySQL View(Merge Profile and Group)
class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"

class GroupWithProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupWithProfile
        fields = "__all__"

