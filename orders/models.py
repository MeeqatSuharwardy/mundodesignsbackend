from django.db import models

class Order(models.Model):
    fullName = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    postcode = models.CharField(max_length=10)
    email = models.EmailField()
    phoneNumber = models.CharField(max_length=20)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_successful = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)  # Instead of ForeignKey, store the product name as a CharField
    quantity = models.IntegerField()
