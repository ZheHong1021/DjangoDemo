from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'users', UserViewSet, basename="user")

urlpatterns = [
    path('', include(router.urls)),


    # 得到當前登入用戶的資訊
    path('current_user/', CurrentUserView.as_view(), name='current_user'),
]