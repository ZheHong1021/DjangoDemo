from rest_framework import serializers
from .models import Menu

class MenuSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        model = Menu
        fields = "__all__"

    def get_children(self, instance):
        return MenuSerializer(instance.children.all(), many=True).data