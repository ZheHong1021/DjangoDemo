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