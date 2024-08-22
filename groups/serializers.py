from rest_framework import serializers
from django.contrib.auth.models import Group
from .models import GroupProfile, GroupWithProfile
from permissions.serializers import PermissionSerializer

# Profile
class GroupProfileSerializer(serializers.ModelSerializer):
    name = serializers.CharField( # Group Name
        source='group.name'
    )
    name_zh = serializers.CharField( # Group Name in Chinese
        required=True
    )

    # 權限
    permissions = serializers.SerializerMethodField()

    class Meta:
        model = GroupProfile
        fields = ['id', 'name', 'name_zh', 'permissions']
    
    # 得到權限數據
    def get_permissions(self, instance):
        return PermissionSerializer(instance.group.permissions.all(), many=True).data
    
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
    def create(self, validated_data):
        group_data = validated_data.pop('group') # 取出 Group Data
        group = Group.objects.create(**group_data) # 創建 Group
        group_profile = GroupProfile.objects.create( # 創建 Group Profile
            group=group, 
            **validated_data
        )
        return group_profile

    def update(self, instance, validated_data):
        group_data = validated_data.pop('group', None) # 取出 Group Data
        if group_data: # 如果有 Group Data
            group = instance.group
            group.name = instance.group.name
            group.save() # 更新 Group
        return super().update(instance, validated_data)


# MySQL View(Merge Profile and Group)
class GroupWithProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupWithProfile
        fields = "__all__"

