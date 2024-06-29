from rest_framework import serializers
from django.contrib.auth.models import Group
from .models import GroupProfile, GroupWithProfile

# Profile
class GroupProfileSerializer(serializers.ModelSerializer):
    # group = serializers.IntegerField(
    #     source='group.id', read_only=True
    # )
    name = serializers.CharField(
        source='group.name'
    )
    name_zh = serializers.CharField(required=True)
    class Meta:
        model = GroupProfile
        fields = ['id', 'name', 'name_zh']
    
    def validate_name(self, value):
        if Group.objects.filter(name__exact=value).exists():
            raise serializers.ValidationError("該角色代號已經存在!")
        return value
    
    def validate_name_zh(self, value):
        if GroupProfile.objects.filter(name_zh__exact=value).exists():
            raise serializers.ValidationError("該角色名稱已經存在!")
        return value

    def create(self, validated_data):
        group_data = validated_data.pop('group')
        group = Group.objects.create(**group_data)
        group_profile = GroupProfile.objects.create(
            group=group, 
            **validated_data
        )
        return group_profile

    def update(self, instance, validated_data):
        group_data = validated_data.pop('group', None)
        if group_data:
            group = instance.group
            group.name = group_data.get('name', group.name)
            group.save()
        return super().update(instance, validated_data)


# MySQL View(Merge Profile and Group)
class GroupWithProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupWithProfile
        fields = "__all__"


#region (內鍵 Group)
# 內建 Group 添加的 Serializers
def get_profile_and_validated_data(validated_data):
    group_validated_data = {}

    # Django內建的column只有 name
    # 先確保傳遞進來的欄位有 name
    if validated_data.get("name"):
        name = validated_data.pop('name') # 透過 pop將 profile給取出並重新定義為一個變數
        group_validated_data = {"name": name}


    # 剩下的欄位就會是 profile的
    profile_data = validated_data

    return profile_data['profile'], group_validated_data
