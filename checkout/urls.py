from django.urls import path
from checkout.views import CheckoutCreateAPIView

urlpatterns = [
    # Other URLs
    path('checkout/', CheckoutCreateAPIView.as_view(), name='checkout-create'),
    path('checkout/<int:order_id>/', CheckoutCreateAPIView.as_view(), name='checkout-create'),
    # Other URLs
]
