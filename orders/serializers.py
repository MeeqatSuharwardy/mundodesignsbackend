from rest_framework import serializers
from .models import Order, OrderItem, Product
import json

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['product', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    items = serializers.JSONField(write_only=True)

    class Meta:
        model = Order
        fields = ['id', 'fullName', 'session_id', 'address', 'postcode', 'email', 'phoneNumber', 'total_price', 'is_successful', 'created_at', 'items']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        for item_data in items_data:
            product_data = item_data.pop('product')
            product_id = product_data.get('id')
            product = Product.objects.get(id=product_id)
            OrderItem.objects.create(order=order, product=product, **item_data)
        return order

