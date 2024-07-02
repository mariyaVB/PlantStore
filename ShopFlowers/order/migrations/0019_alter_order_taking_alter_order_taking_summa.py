# Generated by Django 4.2.1 on 2024-06-25 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0018_alter_order_taking_summa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='taking',
            field=models.CharField(choices=[('Самовывоз', 'Самовывоз'), ('Доставка', 'Доставка')], default='Самовывоз', max_length=150, verbose_name='Тип получения'),
        ),
        migrations.AlterField(
            model_name='order',
            name='taking_summa',
            field=models.CharField(default=0, max_length=10, verbose_name='Сумма доставки'),
        ),
    ]