from rest_framework import generics
from .models import Checkout
from .serializers import CheckoutSerializer
from orders.models import Order

class CheckoutCreateAPIView(generics.CreateAPIView):
    queryset = Checkout.objects.all()
    serializer_class = CheckoutSerializer

    def perform_create(self, serializer):
        order_id = self.request.data.get('order_id')
        order = Order.objects.get(id=order_id)
        serializer.save(order=order)
