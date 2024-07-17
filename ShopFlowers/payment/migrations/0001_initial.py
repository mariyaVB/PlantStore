# Generated by Django 4.2.1 on 2024-07-17 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('order', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentConnectionOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_id', models.CharField(blank=True, max_length=100, null=True, verbose_name='Оплата')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.order', verbose_name='Заказ')),
            ],
            options={
                'verbose_name': 'Связь',
                'verbose_name_plural': 'Связь заказа с оплатой',
            },
        ),
    ]
