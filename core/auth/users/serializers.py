from rest_framework import serializers
from .models import CustomUser

from core.auth.permissions.serializers import PermissionSerializer
from core.auth.groups.serializers import GroupSerializer

from drf_spectacular.utils import extend_schema_field
from drf_spectacular.types import OpenApiTypes

class UserSerializer(serializers.ModelSerializer):
    # 密碼只允許寫入
    password = serializers.CharField(write_only=True, required=False)

    # 全名
    fullname = serializers.SerializerMethodField()

    # 性別顯示
    gender_display = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = "__all__"

    # 取得全名
    @extend_schema_field(OpenApiTypes.STR)
    def get_fullname(self, instance):
        lastname = instance.lastname or ''
        firstname = instance.firstname or ''
        return lastname + firstname

    # 取得性別顯示
    @extend_schema_field(OpenApiTypes.STR)
    def get_gender_display(self, instance):
        return instance.get_gender_display()

    # GET方法取得權限資料
    def to_representation(self, instance):
        representation = super().to_representation(instance)

        # Permission
        representation['user_permissions'] = PermissionSerializer(
            instance.user_permissions.all(), 
            many=True
        ).data

        # Group
        representation['groups'] = GroupSerializer(
            instance.groups.all(), 
            many=True
        ).data
        
        return representation

    # 在寫入前，將資料格式進行調整
    def to_internal_value(self, data):
        #region (權限)
        user_permissions_data = data.get('user_permissions', [])
        # 如果是字串，則轉換成 List
        if isinstance(user_permissions_data, str):
            # 如果確定有值，則轉換成 List，如果為空字串就轉為空List
            data['user_permissions'] = user_permissions_data.split(',')\
                                        if user_permissions_data \
                                        else []
        # 非相對應的資料類型報錯(str / list)
        elif not isinstance(user_permissions_data, list):
            raise serializers.ValidationError("user_permissions 欄位格式錯誤(List or String)")
        #endregion

        #region (權限)
        groups_data = data.get('groups', [])
        # 如果是字串，則轉換成 List
        if isinstance(groups_data, str):
            # 如果確定有值，則轉換成 List，如果為空字串就轉為空List
            data['groups'] = groups_data.split(',')\
                                        if groups_data \
                                        else []
        # 非相對應的資料類型報錯(str / list)
        elif not isinstance(groups_data, list):
            raise serializers.ValidationError("groups 欄位格式錯誤(List or String)")
        #endregion

        return super().to_internal_value(data)
    
    # 創建用戶
    def create(self, validated_data):
        # 將密碼區隔開來
        password = validated_data.pop('password')

        # 權限處理
        user_permissions_data = validated_data.pop('user_permissions', None)
        
        # 角色處理
        groups_data = validated_data.pop('groups', None)
        
        user = CustomUser(**validated_data)
        user.set_password(password) # 再最後設定密碼並且儲存
        user.save()

        # 權限添加(必須等到 user.save() 後才能添加)
        if user_permissions_data is not None:
            user.user_permissions.add(*user_permissions_data) # 添加權限

        # 角色添加(必須等到 user.save() 後才能添加)
        if groups_data is not None:
            user.groups.add(*groups_data) # 添加權限

        return user
    
    # 修改用戶
    def update(self, instance, validated_data):
        #region (Permission)
        # 權限處理
        user_permissions_data = validated_data.pop('user_permissions', None)

        # 如果沒帶入 user_permissions，則不處理
        if user_permissions_data is not None:
            instance.user_permissions.clear() # 清空權限
            instance.user_permissions.add(*user_permissions_data) # 重新設定權限
        #endregion

        #region (Group)
        # 角色處理
        groups_data = validated_data.pop('groups', None)

        # 如果沒帶入 groups，則不處理
        if groups_data is not None:
            instance.groups.clear() # 清空權限
            instance.groups.add(*groups_data) # 重新設定權限
        #endregion

        return super().update(instance, validated_data)