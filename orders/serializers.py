from rest_framework import serializers
from .models import Order
from common.serializers import ReadOnlyIdUserMixin


class OrderSerializer(ReadOnlyIdUserMixin, serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"