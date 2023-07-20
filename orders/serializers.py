from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    items = serializers.ListField(child=serializers.DictField(), write_only=True)

    class Meta:
        model = Order  # Use Order model
        fields = ['id', 'fullName', 'address', 'postcode', 'email', 'phoneNumber', 'total_price',
                  'is_successful', 'created_at', 'items']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)  # Use Order model
        for item_data in items_data:
            OrdersItem.objects.create(order=order, **item_data)  # Use OrdersItem model
        return order
