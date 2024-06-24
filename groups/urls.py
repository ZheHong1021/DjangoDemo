from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'groups', views.GroupViewSet)
router.register(r'group-with-profiles', views.GroupWithProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]