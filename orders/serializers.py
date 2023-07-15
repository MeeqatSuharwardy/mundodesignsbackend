from rest_framework import serializers
from .models import Order, OrderItem
from products.serializers import ProductSerializer
from products.models import Product  # Import the Product model

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['product', 'quantity', 'name', 'image']

class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, read_only=True)  # Set order_items as read-only

    class Meta:
        model = Order
        fields = ['id', 'fullName', 'address', 'email', 'phoneNumber', 'postcode', 'total_price', 'is_successful', 'created_at', 'order_items']
        read_only_fields = ['id', 'is_successful', 'created_at']

    def create(self, validated_data):
        order_items_data = validated_data.pop('order_items')
        order = Order.objects.create(**validated_data)

        for item_data in order_items_data:
            product_data = item_data.pop('product')
            product = Product.objects.create(**product_data)
            OrderItem.objects.create(order=order, product=product, **item_data)

        return order
