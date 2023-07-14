from django.shortcuts import render
from rest_framework import generics
from .models import Order, OrderItem
from .serializers import OrderSerializer, OrderItemSerializer
from products.models import Product

class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        order = serializer.save()
        cart_items = self.request.data.get('cart_items', [])  # Assuming cart_items is sent in the request data
        for cart_item in cart_items:
            product_id = cart_item.get('product_id')
            quantity = cart_item.get('quantity')
            product = Product.objects.get(id=product_id)
            OrderItem.objects.create(order=order, product=product, quantity=quantity)

        # Send email receipt
        # You can use a library like Django's built-in send_mail or a third-party library like Django Mailer or SendGrid
        # Example using Django's send_mail:
        from django.core.mail import send_mail

        subject = 'Order Receipt'
        message = f'Thank you for your order! Your order ID is {order.id}.'
        from_email = 'your@email.com'
        recipient_list = [order.email]

        send_mail(subject, message, from_email, recipient_list)

class OrderRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
