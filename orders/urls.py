from django.urls import path
from .views import OrderListCreateView, OrderRetrieveUpdateDestroyView

urlpatterns = [
    path('order/', OrderListCreateView.as_view(), name='order-list'),
    path('<int:pk>/', OrderRetrieveUpdateDestroyView.as_view(), name='order-detail'),
]
