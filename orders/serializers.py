from rest_framework import serializers
from .models import Order, OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['product_name', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)  # Use OrderItemSerializer to serialize the items

    class Meta:
        model = Order
        fields = ['id', 'fullName', 'session_id', 'address', 'postcode', 'email', 'phoneNumber', 'total_price',
                  'is_successful', 'created_at', 'items']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)
        return order
