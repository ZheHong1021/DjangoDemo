from rest_framework import generics, status, viewsets
from rest_framework.permissions import IsAuthenticated # 權限
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiTypes, OpenApiResponse

from common.paginations import CustomPagination
from common.views import PermissionMixin, SwaggerSchemaMixin

from .models import CustomUser
from .serializers import UserSerializer
from .filters import UserFilter

# 建立訂單 View
@extend_schema(
    tags=['用戶管理'],
    request={
        'multipart/form-data': UserSerializer
    },
)
class UserViewSet(PermissionMixin, SwaggerSchemaMixin, viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination
    filterset_class = UserFilter

    @extend_schema(
        summary="得到所有用戶數據",
        responses={
            200: OpenApiResponse(response=OpenApiTypes.OBJECT, description="成功返回數據"),
            401: OpenApiResponse(description="未授權"),
            403: OpenApiResponse(description="禁止訪問"),
        },
        # parameters=[
        #     OpenApiParameter(
        #         name='param1', description='Description for param1', required=False, type=OpenApiTypes.INT
        #     ),
        #     OpenApiParameter(
        #         name='param2', description='Description for param2', required=False, type=OpenApiTypes.STR
        #     ),
        # ],
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

  