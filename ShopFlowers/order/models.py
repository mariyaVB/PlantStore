from django.db import models
from users.models import User
from cart.models import Cart


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    order = models.ManyToManyField('Order', verbose_name='Заказ', related_name='related_orders')

    class Meta:
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'

    def __str__(self):
        return f'Покупатель {self.user.first_name} {self.user.last_name}'


class Order(models.Model):
    STATUS_NEW = 'new'
    STATUS_IN_PROGRESS = 'in_progress'
    STATUS_IS_READY = 'is_ready'
    STATUS_COMPLETED = 'completed'

    TAKING_TYPE_SELF = 'self'
    TAKING_TYPE_DELIVERY = 'delivery'

    STATUS_CHOICES = (
        (STATUS_NEW, 'Новый заказ'),
        (STATUS_IN_PROGRESS, 'Заказ в обработке'),
        (STATUS_IS_READY, 'Заказ готов'),
        (STATUS_COMPLETED, 'Заказ выполнен')
    )

    TAKING_TYPE_CHOICES = (
        (TAKING_TYPE_SELF, 'Самовывоз'),
        (TAKING_TYPE_DELIVERY, 'Доставка'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', null=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, verbose_name='Корзина', null=True)
    first_name = models.CharField(max_length=250, verbose_name='Имя', blank=True, null=True)
    last_name = models.CharField(max_length=250, verbose_name='Фамилия', blank=True, null=True)
    phone = models.CharField(max_length=11, verbose_name='Номер телефона', blank=True, null=True)
    address = models.CharField(max_length=250, verbose_name='Адрес', blank=True, null=True)
    create_order = models.DateTimeField(auto_now=True, verbose_name='Дата создания заказа')
    ending_order = models.DateTimeField(verbose_name='Дата завершения заказа', blank=True, null=True)
    status = models.CharField(max_length=100,
                              verbose_name='Статус',
                              choices=STATUS_CHOICES,
                              default=STATUS_NEW
                              )
    taking = models.CharField(max_length=100,
                              verbose_name='Тип получения',
                              choices=TAKING_TYPE_CHOICES,
                              default=TAKING_TYPE_DELIVERY
                              )

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return str(self.id)


