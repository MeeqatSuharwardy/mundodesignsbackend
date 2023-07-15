# Generated by Django 4.2.1 on 2023-06-23 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_rename_full_name_checkout_fullname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='checkout',
            old_name='postcode',
            new_name='phoneNumber',
        ),
        migrations.AddField(
            model_name='checkout',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
    ]