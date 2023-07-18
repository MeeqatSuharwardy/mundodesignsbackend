from rest_framework import viewsets
from .models import Order
from .serializers import OrderSerializer
from django.shortcuts import render

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
