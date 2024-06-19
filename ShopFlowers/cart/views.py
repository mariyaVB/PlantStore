from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import Http404
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView
from .models import Cart
from users.models import User
from flowers.models import Flowers
from order.forms import OrderForm


class CartShow(ListView):
    model = Cart
    template_name = 'cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = Cart.objects.filter(user=self.request.user)
        form = OrderForm
        try:
            context['carts'] = cart.filter_status_cart()
            context['form'] = form

            return context
        except:
            raise Http404('Not Found')


class AddCartView(View):
    def get(self, request, product_id):
        product = Flowers.objects.get(id=product_id)
        cart = Cart.objects.filter(user=self.request.user, flowers=product)
        try:
            if not cart.exists():
                Cart.objects.create(user=self.request.user, flowers=product, quantity=1)
            else:
                cart = cart.first()
                cart.quantity += 1
                cart.save()

            return redirect(request.META['HTTP_REFERER'])
        except:
            raise Http404('Not Found')


class RemoveCartView(View):
    def get(self, request, cart_id):
        cart = Cart.objects.filter(id=cart_id)
        try:
            cart.delete()
            messages.add_message(request, messages.SUCCESS, 'Товар удален из корзины.')

            return redirect(request.META['HTTP_REFERER'])
        except:
            raise Http404('Not Found')


class ChangeCartView(View):
    def post(self, request, cart_id):
        self.object = Cart.objects.get(id=cart_id)
        quantity = int(request.POST.get('quantity'))
        try:
            self.object.quantity = quantity
            self.object.save()
            self.object.sum_cart()

            return redirect(request.META['HTTP_REFERER'])
        except:
            raise Http404('Not Found')



