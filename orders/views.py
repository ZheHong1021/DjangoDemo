from .models import Order
from .serializers import OrderSerializer
from rest_framework import generics, status, viewsets
from common.views import CreateWithUserMixin, UpdateWithUserMixin
from rest_framework.permissions import IsAuthenticated # 權限


# 建立訂單 View
class OrderViewSet(
    CreateWithUserMixin, 
    UpdateWithUserMixin,
    viewsets.ModelViewSet
):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated,]