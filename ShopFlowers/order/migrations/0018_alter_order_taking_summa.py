# Generated by Django 4.2.1 on 2024-06-25 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0017_order_taking_summa_alter_order_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='taking_summa',
            field=models.CharField(default=0, max_length=4, verbose_name='Сумма доставки'),
        ),
    ]
