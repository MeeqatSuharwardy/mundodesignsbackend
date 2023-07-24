from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet, create_payment_intent  # Use OrderViewSet

router = DefaultRouter()
router.register(r'orders', OrderViewSet, basename='order')  # Use OrderViewSet

urlpatterns = [
    path('create_payment/', create_payment_intent, name='create_payment'),
] + router.urls
