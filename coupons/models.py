from django.db import models

# Create your models here.


class Coupon(models.Model):
    code = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    min_order_amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_percentage = models.BooleanField(default=False)

    def __str__(self):
        return self.code
