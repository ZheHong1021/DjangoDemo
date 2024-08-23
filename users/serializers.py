from rest_framework import serializers
from .models import CustomUser

from django.contrib.auth.models import Permission
from permissions.serializers import PermissionSerializer

class UserSerializer(serializers.ModelSerializer):
    # 密碼只允許寫入
    password = serializers.CharField(write_only=True, required=False)

    # 全名
    fullname = serializers.SerializerMethodField()

    # 性別顯示
    gender_display = serializers.SerializerMethodField()

    # 權限(多對象)
    # 這邊要寫 permissions 而不是 user_permissions，因為這邊多對象是指 Permission
    permissions = serializers.CharField(
        required=False, allow_blank=True
    )
    
    class Meta:
        model = CustomUser
        fields = "__all__"

    # 取得全名
    def get_fullname(self, instance):
        lastname = instance.lastname or ''
        firstname = instance.firstname or ''
        return lastname + firstname

    # 取得性別顯示
    def get_gender_display(self, instance):
        return instance.get_gender_display()

    # GET方法取得權限資料
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user_permissions'] = PermissionSerializer(
            instance.user_permissions.all(), 
            many=True
        ).data
        return representation

    # 在寫入前，將資料格式進行調整
    def to_internal_value(self, data):
        user_permissions_data = data.get('user_permissions', [])

        # 如果是字串，則轉換成 List
        if isinstance(user_permissions_data, str):
            # 如果確定有值，則轉換成 List，如果為空字串就轉為空List
            data['user_permissions'] = user_permissions_data.split(',')\
                                        if user_permissions_data \
                                        else []
        # 如果是 List，則不用動
        elif isinstance(user_permissions_data, list):
            pass        
        # 非以上兩種資料類型報錯
        else:
            raise serializers.ValidationError("user_permissions 欄位格式錯誤(List or String)")

        return super().to_internal_value(data)
    
    # 創建用戶
    def create(self, validated_data):
        # 將密碼區隔開來
        password = validated_data.pop('password')

        # 權限處理
        user_permissions_data = validated_data.pop('user_permissions', None)
        
        user = CustomUser(**validated_data)
        user.set_password(password) # 再最後設定密碼並且儲存
        user.save()

        # 權限添加(必須等到 user.save() 後才能添加)
        if user_permissions_data is not None:
            user.user_permissions.add(*user_permissions_data) # 添加權限

        return user
    
    # 修改用戶
    def update(self, instance, validated_data):

        # 權限處理
        user_permissions_data = validated_data.pop('user_permissions', None)

        # 如果沒帶入 user_permissions，則不處理
        if user_permissions_data is not None:
            instance.user_permissions.clear() # 清空權限
            instance.user_permissions.add(*user_permissions_data) # 重新設定權限

        return super().update(instance, validated_data)