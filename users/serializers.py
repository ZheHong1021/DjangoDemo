from rest_framework import serializers
from .models import CustomUser


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
      

    def get_fullname(self, instance):
        lastname = instance.lastname or ''
        firstname = instance.firstname or ''
        return lastname + firstname

    def get_gender_display(self, instance):
        return instance.get_gender_display()

    def create(self, validated_data):
        password = validated_data.pop('password') # 將密碼區隔開來
        user = CustomUser(**validated_data)
        user.set_password(password) # 再最後設定密碼並且儲存
        user.save()
        return user