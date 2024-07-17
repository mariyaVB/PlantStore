from django.contrib import admin
from payment.models import PaymentConnectionOrder


@admin.register(PaymentConnectionOrder)
class PaymentConnectionOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'payment_id', 'order')
    list_display_links = ('id', 'payment_id', 'order')
