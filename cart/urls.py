from django.urls import path
from .views import CartListCreateView, CartRetrieveUpdateDestroyView, add_to_cart

urlpatterns = [
    path('', CartListCreateView.as_view(), name='cart-list'),
    path('<int:pk>/', CartRetrieveUpdateDestroyView.as_view(), name='cart-detail'),
    path('add-to-cart/<int:product_id>/<int:quantity>/', add_to_cart, name='add-to-cart'),
]
