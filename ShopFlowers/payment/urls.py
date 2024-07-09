from django.urls import path
import payment.views as payment


urlpatterns = [
    path('webhook/', payment.payment_webhook, name='webhook'),
]
