from rest_framework import serializers
from django.contrib.auth.models import Permission


class PermissionSerializer(serializers.ModelSerializer):
    content_type_name = serializers.CharField(
        read_only=True, required=False
    )
    codename = serializers.CharField(
        read_only=True, required=False
    )
    content_type = serializers.CharField(
        read_only=True, required=False
    )
 
    class Meta:
        model = Permission
        fields = "__all__"
      
