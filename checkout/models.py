from django.db import models
from orders.models import Order

class Checkout(models.Model):
    fullName = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    email = models.EmailField()
    phoneNumber = models.CharField(max_length=20)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='checkouts', null=True)
    totalPrice = models.DecimalField(max_digits=10, decimal_places=2)
