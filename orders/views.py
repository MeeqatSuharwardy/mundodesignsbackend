# views.py
from django.shortcuts import render
from rest_framework import generics
from .models import Order, OrderItem
from .serializers import OrderSerializer, OrderItemSerializer
from products.models import Product
from django.template.loader import render_to_string

class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        order = serializer.save()
        order_items = self.request.data.get('order_items', [])  # Assuming order_items is sent in the request data
        for item in order_items:
            product_name = item.get('product_name')
            product_image = item.get('product_image')
            quantity = item.get('quantity')
            product = Product.objects.create(name=product_name, image=product_image)
            OrderItem.objects.create(order=order, product=product, quantity=quantity)

        # Send email receipt
        from django.core.mail import send_mail

        subject = 'Order Receipt'
        context = {'order': order}
        message = render_to_string('email_receipt.html', context)
        from_email = 'meeqatsuharward@gmail.com'
        recipient_list = [order.email]

        send_mail(subject, message, from_email, recipient_list)

class OrderRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
