from rest_framework import viewsets
from .models import \
            GroupProfile, \
            GroupWithProfile

from .serializers import \
            GroupProfileSerializer, \
            GroupWithProfileSerializer

from .filters import GroupFilter
from common.paginations import CustomPagination
from common.views import SoftDeleteModelViewSet, SwaggerSchemaMixin

from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiTypes, OpenApiResponse

@extend_schema(
    tags=['角色管理'],
    request={
        'multipart/form-data': GroupProfileSerializer
    },
)
class GroupProfileViewSet(SwaggerSchemaMixin, SoftDeleteModelViewSet):
    queryset = GroupProfile.objects.all()
    serializer_class = GroupProfileSerializer


@extend_schema(
    tags=['角色管理'],
    request={
        'multipart/form-data': GroupWithProfileSerializer
    },
)
class GroupWithProfileViewSet(SwaggerSchemaMixin, SoftDeleteModelViewSet):
    queryset = GroupWithProfile.objects.all()
    serializer_class = GroupWithProfileSerializer
    filterset_class = GroupFilter
    pagination_class = CustomPagination