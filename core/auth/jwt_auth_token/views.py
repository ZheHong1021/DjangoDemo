from rest_framework_simplejwt.views import \
        TokenObtainPairView, \
        TokenVerifyView, \
        TokenRefreshView
from rest_framework_simplejwt.serializers import \
        TokenObtainPairSerializer, \
        TokenVerifySerializer, \
        TokenRefreshSerializer

from .serializers import MyTokenObtainPairSerializer


from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiParameter, OpenApiRequest, OpenApiResponse
from drf_spectacular.types import OpenApiTypes

from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed

#region (登入)
@extend_schema_view(
    post=extend_schema(
        tags=['JWT'],
        description='輸入帳號密碼後取得Token',
        request={
            'multipart/form-data': MyTokenObtainPairSerializer
        },
        responses={
            200: OpenApiResponse(response=OpenApiTypes.OBJECT, description="成功登入並取得Token"),
            400: OpenApiResponse(description="無效的請求"),
        }
    ),
)
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
#endregion


#region (驗證Token)
@extend_schema_view(
    post=extend_schema(
        tags=['JWT'],
        description='將 AccessToken進行驗證是否還有效',
        request={
            'multipart/form-data': TokenVerifySerializer
        },
        responses={
            200: OpenApiResponse(response=OpenApiTypes.OBJECT, description="驗證該Token有效"),
            400: OpenApiResponse(description="無效的請求"),
            401: OpenApiResponse(description="憑證失敗"),
        }
    ),
)
class CustomTokenVerifyView(TokenVerifyView):
    pass
#endregion


#region (刷新Token)
@extend_schema_view(
    post=extend_schema(
        tags=['JWT'],
        description='刷新 RefreshToken',
        request={
            'multipart/form-data': TokenRefreshSerializer
        },
        responses={
            200: OpenApiResponse(response=OpenApiTypes.OBJECT, description="成功刷新Token"),
            400: OpenApiResponse(description="無效的請求"),
            401: OpenApiResponse(description="憑證失敗"),
        }
    ),
)
class CustomTokenRefreshView(TokenRefreshView):
    pass
#endregion