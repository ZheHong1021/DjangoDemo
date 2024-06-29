from .models import CustomUser
from .serializers import UserSerializer
from rest_framework import generics, status, viewsets
from rest_framework.permissions import IsAuthenticated # 權限


# 建立訂單 View
class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated,]