# Generated by Django 4.2.1 on 2024-06-18 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0007_remove_cart_flowers_alter_cart_user_cart_flowers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='quantity',
            field=models.PositiveIntegerField(default=0, verbose_name='Количество'),
        ),
    ]
