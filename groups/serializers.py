from rest_framework import serializers
from django.contrib.auth.models import Group
from .models import GroupProfile, GroupWithProfile

# Profile
class GroupProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupProfile
        fields = ['id', 'group', 'name_zh']

# MySQL View(Merge Profile and Group)
class GroupWithProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupWithProfile
        fields = ['id', 'group_name', 'name_zh', 'group_id']


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

class GroupSerializer(serializers.ModelSerializer):
    # profile的欄位
    name = serializers.CharField(
        required=False
    )
    name_zh = serializers.CharField(
        source='profile.name_zh',
        required=False
    )

    class Meta:
        model = Group
        fields = ['name', 'name_zh']  # 根據需要添加其他 GroupProfile 的字段

    def create(self, validated_data):
        profile_data, validated_data = get_profile_and_validated_data(validated_data)

        group = Group.objects.create(**validated_data) # 剩下的validated_data就會只剩 group的
        GroupProfile.objects.create(group=group, **profile_data)
        return group

    def update(self, instance, validated_data):
        profile_data, validated_data = get_profile_and_validated_data(validated_data)

        # 內鍵Group => 只會有 name這個欄位
        instance.name = validated_data.get('name', instance.name)
        instance.save()

        # 找到新對應的 Profile
        profile, created = GroupProfile.objects.get_or_create(group=instance)
        # 可能 profile_data有多個欄位
        for attr, value in profile_data.items():
            # attr: 欄位 ； value: 值
            setattr(profile, attr, value)
        profile.save()

        return instance

#endregion