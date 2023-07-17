from django.db import models

class Order(models.Model):
    full_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    postcode = models.CharField(max_length=10)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_successful = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

class Product(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='products')
    image = models.ImageField(upload_to='product_images')
    title = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.title
