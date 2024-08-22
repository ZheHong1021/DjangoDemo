from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema, OpenApiResponse
from django.contrib.auth.models import Permission
from django.db.models import F

from common.paginations import CustomPagination
from common.views import PermissionMixin, SwaggerSchemaMixin

from .serializers import PermissionSerializer
from .filters import PermissionFilter

@extend_schema(
    tags=['權限管理'],
    request={
        'multipart/form-data': PermissionSerializer
    },
)
class PermissionViewSet(PermissionMixin, SwaggerSchemaMixin, viewsets.ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination
    filterset_class = PermissionFilter

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.annotate(
            content_type_name=F('content_type__model') # 透過外鍵取得(content_type中的name)欄位
        )
        return qs
    