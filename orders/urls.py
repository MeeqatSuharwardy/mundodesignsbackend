from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet, ProductViewSet

router = DefaultRouter()
router.register(r'orders', OrderViewSet, basename='order')
router.register(r'producting', ProductViewSet, basename='product')

urlpatterns = router.urls
