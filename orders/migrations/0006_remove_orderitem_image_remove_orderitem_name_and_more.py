# Generated by Django 4.2.1 on 2023-07-15 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('orders', '0005_orderitem_image_orderitem_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='image',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='name',
        ),
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(through='orders.OrderItem', to='products.product'),
        ),
    ]
