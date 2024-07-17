from django.db import models
from order.models import Order


class PaymentConnectionOrder(models.Model):
    payment_id = models.CharField(max_length=100, verbose_name='Оплата', blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заказ')

    class Meta:
        verbose_name = 'Связь'
        verbose_name_plural = 'Связь заказа с оплатой'
