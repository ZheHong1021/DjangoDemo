from rest_framework import serializers
from .models import Menu

# 沒有 Children
class MenuSerializerWithoutChildren(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = "__all__"

# 有 Children
class MenuSerializerWithChildren(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        model = Menu
        fields = "__all__"

    def get_children(self, instance):
        request = self.context.get('request')
        is_menu = request.query_params.get('is_menu', None)
        if is_menu is not None:
            is_menu = is_menu.lower() == 'true'
            children = instance.children.filter(is_menu=is_menu)
        else:
            children = instance.children.all()
        return MenuSerializerWithChildren(children, many=True, context=self.context).data