from django.db import models

# Create your models here.
from categories.models import Category


class Product(models.Model):
    name = models.CharField(max_length=255)
    categories = models.ManyToManyField(Category)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images')

    def __str__(self):
        return self.name
