# Generated by Django 4.2.1 on 2023-07-17 23:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_product_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
    ]
