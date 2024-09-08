from rest_framework import viewsets

from .serializers import GroupSerializer

from .filters import GroupFilter
from django.contrib.auth.models import Group

from common.paginations import CustomPagination
from common.views import PermissionMixin, SoftDeleteModelViewSet, SwaggerSchemaMixin

from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiTypes, OpenApiResponse

@extend_schema(
    tags=['角色管理'],
    request={
        'multipart/form-data': GroupSerializer
    },
)
class GroupViewSet(PermissionMixin, SwaggerSchemaMixin, viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    filterset_class = GroupFilter

    def get_queryset(self):
        return self.queryset.filter(profile__is_deleted=False)

    def perform_destroy(self, instance):
        # Soft delete the instance
        instance.profile.is_deleted = True
        instance.profile.save()

