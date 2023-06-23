from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Cart
from .serializers import CartSerializer
from products.models import Product
from rest_framework import generics
from rest_framework.permissions import AllowAny

class CartListCreateView(generics.ListCreateAPIView):
    serializer_class = CartSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        session_key = self.request.session.session_key
        return Cart.objects.filter(session_key=session_key)

    def perform_create(self, serializer):
        session_key = self.request.session.session_key
        serializer.save(session_key=session_key)

    def get_total_price(self):
        queryset = self.get_queryset()
        total_price = sum(item.product.price * item.quantity for item in queryset)
        return total_price

class CartRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CartSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        session_key = self.request.session.session_key
        return Cart.objects.filter(session_key=session_key)

@csrf_exempt
def add_to_cart(request, product_id, quantity):
    product = get_object_or_404(Product, id=product_id)

    session_key = request.session.session_key
    if not session_key:
        request.session.create()
        session_key = request.session.session_key

    cart_item, created = Cart.objects.get_or_create(
        session_key=session_key,
        product=product,
        defaults={'quantity': quantity}
    )

    if not created:
        cart_item.quantity += quantity
        cart_item.save()

    serializer = CartSerializer(cart_item)
    return JsonResponse(serializer.data, safe=False)
