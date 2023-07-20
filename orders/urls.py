from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet  # Use OrderViewSet

router = DefaultRouter()
router.register(r'orders', OrderViewSet, basename='order')  # Use OrderViewSet

urlpatterns = router.urls
