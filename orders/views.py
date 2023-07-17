from django.shortcuts import render
from rest_framework import viewsets
from .models import Order, Product
from .serializers import OrderSerializer, ProductSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

def index(request):
    return render(request, 'orders/index.html')
