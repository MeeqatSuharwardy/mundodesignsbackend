from rest_framework import serializers
from .models import Order, OrderItem, Product
import json

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['product', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'fullName', 'session_id', 'address', 'postcode', 'email', 'phoneNumber', 'total_price', 'is_successful', 'created_at', 'items']

    def create(self, validated_data):
        items_data = json.loads(validated_data.pop('items'))
        order = Order.objects.create(**validated_data)
        for item_data in items_data:
            product_data = item_data.pop('product')
            product = Product.objects.create(**product_data)
            OrderItem.objects.create(order=order, product=product, **item_data)
        return order
