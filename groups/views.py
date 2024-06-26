from rest_framework import viewsets
from .models import \
            GroupProfile, \
            GroupWithProfile

from .serializers import \
            GroupProfileSerializer, \
            GroupWithProfileSerializer

from .filters import GroupFilter
from common.paginations import CustomPagination
from common.views import SoftDeleteModelViewSet

class GroupProfileViewSet(SoftDeleteModelViewSet):
    queryset = GroupProfile.objects.all()
    serializer_class = GroupProfileSerializer

class GroupWithProfileViewSet(SoftDeleteModelViewSet, viewsets.ReadOnlyModelViewSet):
    queryset = GroupWithProfile.objects.all()
    serializer_class = GroupWithProfileSerializer
    filterset_class = GroupFilter
    pagination_class = CustomPagination