from django.urls import path
from .views import CouponListCreateView, CouponRetrieveUpdateDestroyView

urlpatterns = [
    path('', CouponListCreateView.as_view(), name='coupon-list'),
    path('<int:pk>/', CouponRetrieveUpdateDestroyView.as_view(), name='coupon-detail'),
]
