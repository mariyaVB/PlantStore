from django.db import models
from users.models import User
from cart.models import Cart


class Order(models.Model):
    STATUS_NEW = 'Создан'
    STATUS_IN_PROGRESS = 'В обработке'
    STATUS_IS_READY = 'Готов'
    STATUS_COMPLETED = 'Выполнен'
    STATUS_CANCEL = 'Отменен'

    TAKING_TYPE_SELF = 'Самовывоз'
    TAKING_TYPE_DELIVERY = 'Доставка'

    STATUS_CHOICES = (
        (STATUS_NEW, 'Создан'),
        (STATUS_IN_PROGRESS, 'В обработке'),
        (STATUS_IS_READY, 'Готов'),
        (STATUS_COMPLETED, 'Выполнен'),
        (STATUS_CANCEL, 'Отменен')
    )

    TAKING_TYPE_CHOICES = (
        (TAKING_TYPE_SELF, 'Самовывоз'),
        (TAKING_TYPE_DELIVERY, 'Доставка'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', null=True)
    cart = models.ManyToManyField(Cart, verbose_name='Корзина для заказа')
    address = models.CharField(max_length=100, verbose_name='Адрес', blank=True, null=True)
    quantity = models.PositiveIntegerField(verbose_name='Количество', null=True)
    summa = models.PositiveIntegerField(verbose_name='Сумма заказа', null=True)
    create_order = models.DateTimeField(auto_now=True, verbose_name='Дата создания заказа')
    ending_order = models.DateTimeField(verbose_name='Дата завершения заказа', blank=True, null=True)
    status = models.CharField(max_length=100,
                              verbose_name='Статус',
                              choices=STATUS_CHOICES,
                              default=STATUS_NEW
                              )
    taking = models.CharField(max_length=150,
                              verbose_name='Тип получения',
                              choices=TAKING_TYPE_CHOICES,
                              default=TAKING_TYPE_SELF
                              )
    taking_summa = models.CharField(max_length=10, verbose_name='Сумма доставки', default=0)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return str(self.id)


