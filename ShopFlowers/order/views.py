from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.db import transaction
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView

from .forms import OrderForm
from cart.models import Cart
from order.models import Order


class MakeOrderView(View):
    @transaction.atomic
    def post(self, request):
        form = OrderForm(request.POST)
        cart = Cart.objects.filter(user=request.user)
        user = self.request.user

        if form.is_valid():
            new_order = form.save(commit=False)
            new_order.user = user
            new_order.first_name = form.cleaned_data['first_name']
            new_order.last_name = form.cleaned_data['last_name']
            new_order.phone = form.cleaned_data['phone']
            new_order.address = form.cleaned_data['address']
            new_order.taking = form.cleaned_data['taking']
            new_order.quantity = cart.total_quantity()
            new_order.summa = cart.total_summ()
            new_order.save()
            new_order.cart.add(*cart)
            new_order.save()

            for el_cart in cart:
                flowers = el_cart.flowers
                flowers.quantity -= el_cart.quantity
                flowers.save()

            for el_cart in cart:
                el_cart.status = 'Оформлен'
                el_cart.save()

            return HttpResponseRedirect(reverse_lazy('main'))
        return HttpResponseRedirect(reverse_lazy('cart'))


class OrderProfileView(ListView):
    model = Order
    template_name = 'profile_order.html'
    context_object_name = 'orders'
    paginate_by = 3

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


