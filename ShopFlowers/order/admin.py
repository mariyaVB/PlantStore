from django.contrib import admin
from .models import Customer, Order


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')
    list_display_links = ('id', 'user')
    verbose_name = 'Покупатели'


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'cart', 'phone', 'address', 'status', 'taking', 'create_order', 'ending_order')
    list_display_links = ('id', 'cart', 'user')
    verbose_name = 'Заказы'
