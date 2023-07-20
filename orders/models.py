from django.db import models

class Order(models.Model):  # Use the class name 'Order'
    fullName = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    postcode = models.CharField(max_length=10)
    email = models.EmailField()
    phoneNumber = models.CharField(max_length=20)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_successful = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    # Fields for Order Items
    product_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
