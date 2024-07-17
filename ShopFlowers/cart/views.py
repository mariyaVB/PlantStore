from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
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
        cart = Cart.objects.filter(user=self.request.user)
        form = OrderForm
        context['carts'] = cart.filter_status_cart()
        context['form'] = form

        return context


class AddCartView(LoginRequiredMixin, View):
    def get(self, request, product_id):
        product = Flowers.objects.get(id=product_id)
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
        cart = Cart.objects.filter(id=cart_id)
        try:
            cart.delete()
            messages.add_message(request, messages.SUCCESS, 'Товар удален из корзины.')

            return redirect(request.META['HTTP_REFERER'])
        except cart.DoesNotExist:
            raise Http404('Ошибка при удалении корзины')


class ChangeCartView(View):
    def post(self, request, cart_id):
        self.object = Cart.objects.get(id=cart_id)
        quantity = int(request.POST.get('quantity'))
        self.object.quantity = quantity
        self.object.save()
        self.object.sum_cart()

        return redirect(request.META['HTTP_REFERER'])




