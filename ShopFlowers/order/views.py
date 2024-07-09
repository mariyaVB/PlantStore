import os
import uuid
import datetime
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.db import transaction, IntegrityError
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView
from .forms import OrderForm
from feedback.forms import AddFeedbackForm
from cart.models import Cart
from order.models import Order
from payment.views import create_payment
from payment.models import PaymentConnectionOrder
from dotenv import load_dotenv
from yookassa import Payment, Configuration, Refund
from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.core.serializers import serialize
from django.core import serializers
import json


load_dotenv()
Configuration.account_id = os.getenv('DJANGO_YOOKASSA_SHOP_ID')
Configuration.secret_key = os.getenv('DJANGO_YOOKASSA_SECRET_KEY')


class AddOrderView(View):
    """ Сохраняем заказ """
    @transaction.atomic
    def post(self, request):
        user = self.request.user
        form = OrderForm(request.POST)
        cart = Cart.objects.filter(user=request.user, status='В корзине')
        if form.is_valid() and cart:
            new_order = form.save(commit=False)
            new_order.user = user
            new_order.address = form.cleaned_data['address']
            new_order.taking = form.cleaned_data['taking']
            new_order.taking_summa = form.cleaned_data['taking_summa']
            new_order.status_payment = form.cleaned_data['payment']
            new_order.quantity = cart.total_quantity()
            new_order.summa = form.cleaned_data['summa']
            new_order.save()
            new_order.cart.add(*cart)
            new_order.save()
            if new_order.payment == 'Онлайн':
                try:
                    payment = create_payment(new_order.summa, new_order.id, user.id)
                    return redirect(payment.confirmation.confirmation_url)
                except IntegrityError:
                    return redirect('cart:cart')

            else:
                new_order.status_payment = 'Не оплачен'
                new_order.save()
                for el_cart in cart:
                    flowers = el_cart.flowers
                    flowers.quantity -= el_cart.quantity
                    el_cart.status = 'Оформлен'
                    flowers.save()
                    el_cart.save()
                new_order.status_payment = 'Не оплачен'
                new_order.save()

                data = {
                    'user': user,
                    'order': new_order,
                }

                email_html = render_to_string('email_order.html', data)
                msg = EmailMultiAlternatives(subject='Уведомление о заказе на сайте FreshCompany', to=[f'{user.email}'])
                msg.attach_alternative(email_html, 'text/html')
                msg.send()

            return HttpResponseRedirect(reverse_lazy('order:order-profile'))

        messages.add_message(request, messages.SUCCESS, 'Ваша корзина пуста или адрес заполнен не правильно.')
        return HttpResponseRedirect(reverse_lazy('cart:cart'))


class OrderProfileView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'profile_order.html'
    context_object_name = 'orders'
    paginate_by = 4

    def get_queryset(self):
        order = Order.objects.filter(user=self.request.user).exclude(status_order='Отменен').order_by('-create_order')
        return order

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = AddFeedbackForm
        context['form'] = form
        return context


class CancelOrderView(ListView):
    def get(self, request, order_id):
        user = self.request.user
        order = Order.objects.get(id=order_id)
        order.status_order = 'Отменен'
        order.ending_order = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        order.save()
        for cart in order.cart.all():
            flowers = cart.flowers
            flowers.quantity += cart.quantity
            flowers.save()

        if order.payment == 'Онлайн':
            """ Возврат оплаты """
            payment = PaymentConnectionOrder.objects.get(order=order.id)
            Refund.create({
                "amount": {
                    "value": order.summa,
                    "currency": "RUB",
                    "description": "Возврат денежных средств за заказ на сайте FreshCompany",
                },
                "payment_id": payment.payment_id
            })

            data = {
                'user': user,
                'order': order,
            }

            email_html = render_to_string('email_cancel_order.html', data)
            msg = EmailMultiAlternatives(subject='Уведомление о отмене заказа на сайте FreshCompany', to=[f'{user.email}'])
            msg.attach_alternative(email_html, 'text/html')
            msg.send()

            messages.add_message(request, messages.SUCCESS, 'Ваш заказ успешно отменен.')
            return redirect(request.META['HTTP_REFERER'])
        data = {
            'user': user,
            'order': order,
        }

        email_html = render_to_string('email_cancel_order.html', data)
        msg = EmailMultiAlternatives(subject='Уведомление о отмене заказа на сайте FreshCompany', to=[f'{user.email}'])
        msg.attach_alternative(email_html, 'text/html')
        msg.send()

        messages.add_message(request, messages.SUCCESS, 'Ваш заказ успешно отменен.')
        return HttpResponseRedirect(reverse_lazy('order:order-profile'))

