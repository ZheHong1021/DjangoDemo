from rest_framework import viewsets, status
from rest_framework.response import Response
from django.contrib.auth.models import Group

from .models import GroupProfile, GroupWithProfile
from .serializers import \
            GroupProfileSerializer, \
            GroupWithProfileSerializer
            # GroupSerializer, \

from .filters import GroupFilter
from common.paginations import CustomPagination

class GroupProfileViewSet(viewsets.ModelViewSet):
    queryset = GroupProfile.objects.all()
    serializer_class = GroupProfileSerializer


class GroupWithProfileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = GroupWithProfile.objects.all()
    serializer_class = GroupWithProfileSerializer
    filterset_class = GroupFilter
    pagination_class = CustomPagination



# class GroupViewSet(viewsets.ModelViewSet):
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer

#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)
#         headers = self.get_success_headers(serializer.data)
#         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

