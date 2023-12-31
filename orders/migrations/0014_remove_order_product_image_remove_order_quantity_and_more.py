# Generated by Django 4.2.1 on 2023-07-18 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0013_remove_orderitem_product_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='product_image',
        ),
        migrations.RemoveField(
            model_name='order',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='order',
            name='title',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='product_id',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderitem',
            name='session_id',
            field=models.CharField(default='default_session_id', max_length=100),
        ),
    ]
