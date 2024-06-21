from rest_framework import serializers

# Serializer中只能針對 id、user進行讀取而已 (無法寫入)
class ReadOnlyIdUserMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 只能讀取以下欄位
        for field_name in ('id', 'user'):
            if field_name in self.fields:
                self.fields[field_name].read_only = True