from rest_framework import serializers, viewsets


# [創建時] 儲存使用者ID
class CreateWithUserMixin:
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# [修改時] 儲存使用者ID
class UpdateWithUserMixin:
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


# 軟刪除
class SoftDeleteModelViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        # Only return objects that are not soft deleted
        return self.queryset.filter(is_deleted=False)

    def perform_destroy(self, instance):
        # Soft delete the instance
        instance.is_deleted = True
        instance.save()



from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiRequest, OpenApiResponse
from drf_spectacular.types import OpenApiTypes

# [Swagger UI For ModelViewSet]
class SwaggerSchemaMixin:
    model_class = None
    serializer_class = None
    list_parameters = []
    list_summary = "得到所有數據"
    detail_summary = "得到特定ID的數據"
    create_summary = "創建數據"
    update_summary = "修改數據"
    delete_summary = "刪除數據"

    #region (List)
    @extend_schema(
        summary=list_summary,
        responses={
            200: OpenApiResponse(response=OpenApiTypes.OBJECT, description="成功返回數據"),
            401: OpenApiResponse(description="未授權"),
            403: OpenApiResponse(description="禁止訪問"),
        }
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    #endregion

    #region (retrieve)
    @extend_schema(
        summary=detail_summary,
        responses={
            200: OpenApiResponse(response=OpenApiTypes.OBJECT, description="成功返回特定數據"),
            404: OpenApiResponse(description="找不到為該ID的數據"),
        }
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    #endregion


    #region (create)
    @extend_schema(
        summary=create_summary,
        responses={
            201: OpenApiResponse(response=OpenApiTypes.OBJECT, description="成功創建數據"),
            400: OpenApiResponse(description="無效的請求"),
        }
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    #endregion

    #region (update)
    @extend_schema(
        summary=update_summary,
        # request=OpenApiTypes.OBJECT,
        responses={
            200: OpenApiResponse(response=OpenApiTypes.OBJECT, description="成功修改數據"),
            400: OpenApiResponse(description="無效的請求"),
            404: OpenApiResponse(description="找不到為該ID的數據"),
        }
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    #endregion

    #region (delete)
    @extend_schema(
        summary=delete_summary,
        responses={
            204: OpenApiResponse(description="成功刪除數據"),
            404: OpenApiResponse(description="找不到為該ID的數據"),
        }
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    #endregion