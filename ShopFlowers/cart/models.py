from django.db import models
from users.models import User
from flowers.models import Flowers


class CartQuerySet(models.QuerySet):
    def total_summ(self):
        return sum(cart.sum_cart() for cart in self)

    def total_quantity(self):
        return sum(cart.quantity for cart in self)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    flowers = models.ManyToManyField('Flowers', verbose_name='Растение')
    # flowers = models.ForeignKey(Flowers, on_delete=models.CASCADE, verbose_name='Растение')
    quantity = models.PositiveIntegerField(default=0)

    objects = CartQuerySet.as_manager()

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    def __str__(self):
        return str(self.id)

    def sum_cart(self):
        return self.flowers.price * self.quantity




