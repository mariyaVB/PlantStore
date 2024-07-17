# Generated by Django 4.2.1 on 2024-07-16 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=100, null=True, verbose_name='Адрес')),
                ('quantity', models.PositiveIntegerField(null=True, verbose_name='Количество')),
                ('summa', models.PositiveIntegerField(null=True, verbose_name='Сумма заказа')),
                ('taking_summa', models.CharField(default=0, max_length=10, verbose_name='Сумма доставки')),
                ('create_order', models.DateTimeField(auto_now=True, verbose_name='Дата создания заказа')),
                ('ending_order', models.DateTimeField(blank=True, null=True, verbose_name='Дата завершения заказа')),
                ('status_order', models.CharField(choices=[('Создан', 'Создан'), ('В обработке', 'В обработке'), ('Готов', 'Готов'), ('Выполнен', 'Выполнен'), ('Отменен', 'Отменен')], default='Создан', max_length=100, verbose_name='Статус заказа')),
                ('taking', models.CharField(choices=[('Самовывоз', 'Самовывоз'), ('Доставка', 'Доставка')], default='Самовывоз', max_length=150, verbose_name='Тип получения')),
                ('payment', models.CharField(choices=[('При получении', 'При получении'), ('Онлайн', 'Онлайн')], default='При получении', max_length=150, verbose_name='Тип оплаты')),
                ('status_payment', models.CharField(choices=[('Не оплачен', 'Не оплачен'), ('Оплачен', 'Оплачен')], default='Не оплачен', max_length=100, verbose_name='Статус оплаты')),
                ('is_payment', models.BooleanField(default=False, verbose_name='Оплата')),
                ('cart', models.ManyToManyField(to='cart.cart', verbose_name='Корзина для заказа')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
    ]
