# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenVerifyView,
#     TokenRefreshView,
# )
from .views import *
from django.urls import path, include

urlpatterns = [
    path('', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('verify/', CustomTokenVerifyView.as_view(), name='token_verify'),
    path('refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
]