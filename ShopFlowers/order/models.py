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

    PAYMENT_TYPE_RECEIPT = 'При получении'
    PAYMENT_TYPE_ONLINE = 'Онлайн'

    PAYMENT_TYPE_CHOICES = (
        (PAYMENT_TYPE_RECEIPT, 'При получении'),
        (PAYMENT_TYPE_ONLINE, 'Онлайн'),
    )

    STATUS_NOT_PAYMENT = 'Не оплачен'
    STATUS_PAYMENT = 'Оплачен'

    STATUS_PAYMENT_CHOICES = (
        (STATUS_NOT_PAYMENT, 'Не оплачен'),
        (STATUS_PAYMENT, 'Оплачен'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', null=True)
    cart = models.ManyToManyField(Cart, verbose_name='Корзина для заказа')
    address = models.CharField(max_length=100, verbose_name='Адрес', blank=True, null=True)
    quantity = models.PositiveIntegerField(verbose_name='Количество', null=True)
    summa = models.PositiveIntegerField(verbose_name='Сумма заказа', null=True)
    taking_summa = models.CharField(max_length=10, verbose_name='Сумма доставки', default=0)
    create_order = models.DateTimeField(auto_now=True, verbose_name='Дата создания заказа')
    ending_order = models.DateTimeField(verbose_name='Дата завершения заказа', blank=True, null=True)
    status_order = models.CharField(max_length=100,
                                    verbose_name='Статус заказа',
                                    choices=STATUS_CHOICES,
                                    default=STATUS_NEW
                                    )
    taking = models.CharField(max_length=150,
                              verbose_name='Тип получения',
                              choices=TAKING_TYPE_CHOICES,
                              default=TAKING_TYPE_SELF
                              )
    payment = models.CharField(max_length=150,
                               verbose_name='Тип оплаты',
                               choices=PAYMENT_TYPE_CHOICES,
                               default=PAYMENT_TYPE_RECEIPT
                               )
    status_payment = models.CharField(max_length=100,
                                      verbose_name='Статус оплаты',
                                      choices=STATUS_PAYMENT_CHOICES,
                                      default=STATUS_NOT_PAYMENT
                                      )
    is_payment = models.BooleanField(verbose_name='Оплата', default=False)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return str(self.id)






