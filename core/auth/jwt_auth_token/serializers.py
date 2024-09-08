from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import status

from core.auth.users.models import CustomUser
from django.contrib.auth.hashers import check_password


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        # token['name'] = user.firstname
        # ...

        return token
    
    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        # 手動查詢用戶
        try:
            user = CustomUser.objects.get(username=username)
        except CustomUser.DoesNotExist:
            raise AuthenticationFailed('帳號或密碼不正確')

        # 檢查用戶是否被停用
        if not user.is_active:
            raise AuthenticationFailed('您的帳號已被停用，請聯繫管理員。')

        # 檢查密碼是否正確
        if not check_password(password, user.password):
            raise AuthenticationFailed('帳號或密碼不正確')

        # 如果用戶通過驗證，則調用父類的 validate 方法
        data = super().validate(attrs)
        return data
