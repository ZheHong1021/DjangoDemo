from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'products/category', ProductCategoryViewSet, basename="product-category")
router.register(r'products', ProductViewSet, basename="products")

urlpatterns = [
    path('', include(router.urls)),
]