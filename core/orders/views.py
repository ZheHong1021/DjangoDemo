from rest_framework import generics, status, viewsets
from rest_framework.permissions import IsAuthenticated # 權限
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiTypes, OpenApiResponse

from common.views import PermissionMixin, CreateWithUserMixin, UpdateWithUserMixin
from common.paginations import CustomPagination

from .models import Order
from .serializers import OrderSerializer
from .filters import OrderFilter

# 建立訂單 View
@extend_schema(
    tags=['訂單管理'],
    request={
        'multipart/form-data': OrderSerializer
    },
)
class OrderViewSet(
    PermissionMixin,
    CreateWithUserMixin, 
    UpdateWithUserMixin,
    viewsets.ModelViewSet
):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated,]
    pagination_class = CustomPagination
    filterset_class = OrderFilter
