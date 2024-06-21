from .models import Order
from .serializers import OrderSerializer
from rest_framework import generics, status, viewsets


# 建立訂單 View
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer