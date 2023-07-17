from rest_framework import serializers
from .models import Order, Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = '__all__'
        extra_kwargs = {
            'email': {'write_only': True}  # Ensure the email field is write-only
        }

    def create(self, validated_data):
        products_data = validated_data.pop('products', [])
        order = Order.objects.create(**validated_data)
        for product_data in products_data:
            Product.objects.create(order=order, **product_data)
        return order