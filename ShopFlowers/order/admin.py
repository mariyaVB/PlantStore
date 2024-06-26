from django.contrib import admin
from .models import Order

class OrderInline(admin.TabularInline):
    model = Order.cart.through
    extra = 0  # Не показывать дополнительные пустые формы для создания корзин
    verbose_name = 'Связанные корзины с заказом'
    verbose_name_plural = 'Связанные корзины с заказом'


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderInline]
    exclude = ('cart',)
    list_display = ('id', 'user', 'status', 'quantity', 'summa', 'taking', 'create_order', 'ending_order', 'taking_summa')
    list_display_links = ('id', 'user')
    list_filter = ['id', 'status']
    verbose_name = 'Заказы'

