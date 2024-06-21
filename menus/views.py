from rest_framework import viewsets
from .models import Menu
from .serializers import MenuSerializer
from .filters import MenuFilter
from common.paginations import CustomPagination

class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    filterset_class = MenuFilter
    pagination_class = CustomPagination