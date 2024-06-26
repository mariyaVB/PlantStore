from django.contrib import admin
from .models import Cart


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'flowers', 'quantity')
    list_display_links = ('id', 'user')
    verbose_name = 'Корзины'

