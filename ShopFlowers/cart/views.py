from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView
from .models import Cart
from flowers.models import Flowers
from order.forms import OrderForm
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class CartShow(LoginRequiredMixin, ListView):
    model = Cart
    template_name = 'cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        carts = Cart.objects.filter(user=self.request.user).filter_status_cart()
        for cart in carts:
            if cart.flowers.quantity <= 0:
                cart.delete()

        new_carts = Cart.objects.filter(user=self.request.user).filter_status_cart()
        form = OrderForm
        context['carts'] = new_carts
        context['form'] = form

        return context


class AddCartView(LoginRequiredMixin, View):
    def get(self, request, product_id):
        try:
            product = Flowers.objects.get(id=product_id)
        except Flowers.DoesNotExist:
            return Http404('Продукт не найден')

        cart = Cart.objects.filter(user=self.request.user, flowers=product, status='В корзине')
        if not cart.exists():
            Cart.objects.create(user=self.request.user, flowers=product, quantity=1)
        else:
            cart = cart.first()
            if cart.quantity < product.quantity:
                cart.quantity += 1
                cart.save()
            else:
                pass

        return redirect(request.META['HTTP_REFERER'])


class RemoveCartView(View):
    def get(self, request, cart_id):
        try:
            cart = Cart.objects.filter(id=cart_id)
            cart.delete()
        except Cart.DoesNotExist:
            print('Корзина для удаления не найдена')
            return Http404('Корзина для удаления не найдена')

        messages.add_message(request, messages.SUCCESS, 'Товар удален из корзины.')
        return redirect(request.META['HTTP_REFERER'])


class ChangeCartView(View):
    def post(self, request, cart_id):
        self.object = Cart.objects.get(id=cart_id)
        quantity = int(request.POST.get('quantity'))
        self.object.quantity = quantity
        self.object.save()
        self.object.sum_cart()

        return redirect(request.META['HTTP_REFERER'])




