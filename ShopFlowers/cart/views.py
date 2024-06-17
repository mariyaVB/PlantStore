from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, request
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from .models import Cart
from users.models import User
from flowers.models import Flowers
from order.forms import OrderForm


class CartShow(ListView):
    model = Cart
    template_name = 'cart.html'
    context_object_name = 'carts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = Cart.objects.filter(user=self.request.user)
        form = OrderForm
        context['carts'] = cart
        context['form'] = form
        return context


class AddCartView(View):
    def get(self, request, product_id):
        product = Flowers.objects.get(id=product_id)
        cart = Cart.objects.filter(user=self.request.user, flowers=product)

        if not cart.exists():
            Cart.objects.create(user=self.request.user, flowers=product, quantity=1)
        else:
            cart = cart.first()
            cart.quantity += 1
            cart.save()

        return redirect(request.META['HTTP_REFERER'])


class RemoveCartView(View):
    def get(self, request, cart_id):
        cart = Cart.objects.filter(id=cart_id)
        cart.delete()

        return redirect(request.META['HTTP_REFERER'])


class ChangeCartView(View):
    def post(self, request, cart_id):
        self.object = Cart.objects.get(id=cart_id)
        quantity = int(request.POST.get('quantity'))
        self.object.quantity = quantity
        self.object.save()
        self.object.sum_cart()

        return redirect(request.META['HTTP_REFERER'])


