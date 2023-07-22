from django.core.mail import send_mail
from rest_framework import serializers
from .models import Order, OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['product_name', 'quantity', 'price', 'product_id']

class OrderSerializer(serializers.ModelSerializer):
    # Change 'write_only' to False to include items in response (GET requests)
    items = OrderItemSerializer(many=True, read_only=False)

    class Meta:
        model = Order
        fields = ['id', 'fullName', 'address', 'postcode', 'email', 'phoneNumber', 'total_price',
                  'is_successful', 'created_at', 'items']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)

        # Send email of the invoice when the order is placed
        subject = 'Invoice for your order'
        message = f'Thank you for your order, {order.fullName}! \n\n' \
                  f'Order ID: {order.id} \n' \
                  f'Total Price: {order.total_price} \n\n' \
                  'Your order details:\n'
        for item in order.items.all():
            message += f' - {item.product_name} (Quantity: {item.quantity}, Price: {item.price})\n'

        send_mail(
            subject=subject,
            message=message,
            from_email='your@example.com',  # Replace this with your email
            recipient_list=[order.email],
            fail_silently=True,
        )

        return order
