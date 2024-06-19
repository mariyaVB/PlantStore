from django.contrib import messages
from django.http import HttpResponseRedirect, Http404, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.db import transaction
from django.template.context_processors import request
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView
from .forms import OrderForm
from cart.models import Cart
from order.models import Order


def error_404(request, exception):
    return render(request, '404.html', status=404)


class AddOrderView(View):
    @transaction.atomic
    def post(self, request):
        form = OrderForm(request.POST)
        cart = Cart.objects.filter(user=request.user, status='В корзине')
        user = self.request.user
        try:
            if form.is_valid() and cart:
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

                return HttpResponseRedirect(reverse_lazy('order-profile'))
        except:
            raise Http404('Not Found')
        return HttpResponseRedirect(reverse_lazy('cart'))


class OrderProfileView(ListView):
    model = Order
    template_name = 'profile_order.html'
    context_object_name = 'orders'
    paginate_by = 4

    def get_queryset(self):
        try:
            return Order.objects.filter(user=self.request.user).exclude(status='Отменен')
        except:
            raise Http404('Not Found')


class CancelOrderView(ListView):
    def get(self, request, order_id):
        order = Order.objects.get(id=order_id)
        try:
            order.status = 'Отменен'
            order.save()
            for cart in order.cart.all():
                flowers = cart.flowers
                flowers.quantity += cart.quantity
                flowers.save()

                messages.add_message(request, messages.SUCCESS, 'Ваш заказ успешно отменен.')
                return redirect(request.META['HTTP_REFERER'])
        except:
            raise Http404('Not Found')

        return HttpResponseRedirect(reverse_lazy('order-profile'))

