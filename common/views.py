from rest_framework import serializers


# [創建時] 儲存使用者ID
class CreateWithUserMixin:
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# [修改時] 儲存使用者ID
class UpdateWithUserMixin:
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)