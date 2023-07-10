from rest_framework import serializers
from .models import Order, OrderItem
from products.serializers import ProductSerializer

class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = OrderItem
        fields = ['product', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    orderitem_set = OrderItemSerializer(many=True, source='orderitem_set.all')

    class Meta:
        model = Order
        fields = ['id', 'fullName', 'address', 'email', 'phoneNumber', 'orderitem_set', 'total_price', 'is_successful', 'created_at']
        read_only_fields = ['id', 'is_successful', 'created_at']
