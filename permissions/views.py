from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from common.paginations import CustomPagination
from common.views import PermissionMixin, SwaggerSchemaMixin

from drf_spectacular.utils import extend_schema, OpenApiResponse

from django.contrib.auth.models import Permission
from .serializers import PermissionSerializer

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