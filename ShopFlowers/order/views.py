from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.db import transaction
from django.urls import reverse_lazy
from django.views import View
from .forms import OrderForm
from .models import Order, Customer
from cart.models import Cart
from users.models import User


class MakeOrderView(View):
    @transaction.atomic
    def post(self, request):
        form = OrderForm(request.POST)
        cart = Cart.objects.get(user=request.user)
        user = self.request.user

        if form.is_valid():
            new_order = form.save(commit=False)
            new_order.user = user
            new_order.first_name = form.cleaned_data['first_name']
            new_order.last_name = form.cleaned_data['last_name']
            new_order.phone = form.cleaned_data['phone']
            new_order.address = form.cleaned_data['address']
            new_order.taking = form.cleaned_data['taking']
            new_order.save()
            new_order.cart = cart
            new_order.save()
            # customer.order.add(new_order)
            return HttpResponseRedirect(reverse_lazy('main'))
        return HttpResponseRedirect(reverse_lazy('cart'))


