from django.db import models
from products.models import Product

class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    session_key = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f'{self.session_key} - {self.product.name}'

    @property
    def image(self):
        return self.product.image

    @property
    def description(self):
        return self.product.description

    @property
    def price(self):
        return self.product.price
