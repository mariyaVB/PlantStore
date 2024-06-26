# Generated by Django 4.2.1 on 2024-06-17 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_alter_customer_options_alter_order_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Адрес'),
        ),
        migrations.AddField(
            model_name='order',
            name='first_name',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='order',
            name='last_name',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Фамилия'),
        ),
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='Номер телефона'),
        ),
    ]
