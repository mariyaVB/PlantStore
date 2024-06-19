from django.db import models
from users.models import User
from flowers.models import Flowers


class CartQuerySet(models.QuerySet):
    def total_summ(self):
        return sum(cart.sum_cart() for cart in self)

    def total_quantity(self):
        return sum(cart.quantity for cart in self)

    def filter_status_cart(self):
        return self.filter(status='В корзине')


class Cart(models.Model):
    STATUS_IN_CART = 'В корзине'
    STATUS_ORDERED = 'Оформлен'

    STATUS_CHOICES = (
        (STATUS_IN_CART, 'В корзине'),
        (STATUS_ORDERED, 'Оформлен'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    flowers = models.ForeignKey(Flowers, on_delete=models.CASCADE, verbose_name='Растение', null=True)
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    status = models.CharField(max_length=20,
                              verbose_name='Статус корзины',
                              choices=STATUS_CHOICES,
                              default=STATUS_IN_CART
                              )
    objects = CartQuerySet.as_manager()

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    def __str__(self):
        return str(self.id)

    def sum_cart(self):
        return self.flowers.price * self.quantity




