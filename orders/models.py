from django.db import models
from products.models import Product

class Order(models.Model):
    fullName = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    email = models.EmailField()
    phoneNumber = models.CharField(max_length=20)
    products = models.ManyToManyField(Product, through='OrderItem')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_successful = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.fullName} - {self.id}'

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.order} - {self.product.name}'
