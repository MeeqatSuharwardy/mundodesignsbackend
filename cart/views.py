from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Cart
from .serializers import CartSerializer
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Product

class CartListCreateView(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


def add_to_cart(request, product_id, quantity):
    product = get_object_or_404(Product, id=product_id)

    # Create the cart item
    cart_item = Cart(product=product, quantity=quantity)
    cart_item.save()

    return JsonResponse({'message': 'Product added to cart.'})