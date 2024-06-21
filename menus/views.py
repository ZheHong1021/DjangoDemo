from rest_framework import viewsets
from .models import Menu
from .serializers import \
    MenuSerializerWithoutChildren, \
    MenuSerializerWithChildren
from .filters import MenuFilter
from common.paginations import CustomPagination

class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    filterset_class = MenuFilter
    pagination_class = CustomPagination

    # 將query傳遞給 Serializer
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context
    
    # 挑選要哪一個
    def get_serializer_class(self):
        include_children = self.request.query_params.get('include_children', 'false').lower() == 'true'
        if include_children:
            return MenuSerializerWithChildren
        return MenuSerializerWithoutChildren