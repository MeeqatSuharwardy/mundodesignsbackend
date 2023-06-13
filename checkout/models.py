from django.db import models


# Create your models here.

class Checkout(models.Model):
    full_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    postcode = models.CharField(max_length=20)
    order = models.ForeignKey('orders.Order', on_delete=models.CASCADE, related_name='checkouts', null=True)
