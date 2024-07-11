import os
import json
from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from dotenv import load_dotenv
from yookassa import Payment, Configuration
from cart.models import Cart
from payment.models import PaymentConnectionOrder
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from order.models import Order
from users.models import User

import logging
import uuid
from django.shortcuts import render, redirect, get_object_or_404


load_dotenv()
Configuration.account_id = os.getenv('DJANGO_YOOKASSA_SHOP_ID')
Configuration.secret_key = os.getenv('DJANGO_YOOKASSA_SECRET_KEY')

logger = logging.getLogger(__name__)


def create_payment(summa, metadata):
    """ Создание оплаты """
    idempotence_key = str(uuid.uuid4())

    payment = Payment.create({
        "amount": {
            "value": summa,
            "currency": "RUB"
        },
        "confirmation": {
            "type": "redirect",
            "return_url": "https://06b0-95-58-138-130.ngrok-free.app/order/order_profile/"
        },
        "capture": True,
        "description": "Оплата на сайте FreshCompany",
        "metadata": metadata,
    }, idempotence_key)

    return payment



#     """ Создание оплаты """
#     metadata = {
#         "user": user,
#         "order": order,
#     }
#     idempotence_key = str(uuid.uuid4())
#
#     payment = Payment.create({
#         "amount": {
#             "value": summa,
#             "currency": "RUB"
#         },
#         "confirmation": {
#             "type": "redirect",
#             "return_url": "https://06b0-95-58-138-130.ngrok-free.app/order/order_profile/"
#         },
#         "capture": True,
#         "description": "Оплата на сайте FreshCompany",
#         "metadata": metadata,
#     }, idempotence_key)
#     return payment

#
# @csrf_exempt
# def payment_webhook(request):
#     if request.method == 'POST':
#         try:
#             payment_json = json.loads(request.body)
#         except json.JSONDecodeError:
#             return HttpResponse(status=400)
#
#         payment_object = payment_json['object']
#         payment_id = payment_object['id']
#         print(f"Payment id: {payment_id}")
#
#         payment_status = payment_object['status']
#         print(f"Payment status: {payment_status}")
#
#         user_id = int(payment_object['metadata']['user_id'])
#         print(f"User id: {user_id} and type: {type(user_id)}")
#         payment_user = get_object_or_404(User, id=user_id)
#         print(payment_user)
#
#         if payment_status == 'succeeded':
#             Order.objects.create(
#                 user=payment_user,
#                 address=payment_object['metadata']['address'],
#                 taking=payment_object['metadata']['taking'],
#                 summa=payment_object['amount']['value'],
#                 taking_summa=payment_object['metadata']['taking_summa'],
#                 quantity=payment_object['metadata']['quantity'],
#                 is_payment=True,
#                 payment='Онлайн',
#                 status_payment='Оплачен'
#             )
#
#             cart = Cart.objects.filter(user=payment_user, status='В корзине')
#             order = Order.objects.filter(user=payment_user).last()
#             order.cart.add(*cart)
#             order.save()
#
#             PaymentConnectionOrder.objects.create(payment_id=payment_id, order=order.id)
#
#             for cart in order.cart.all():
#                 flowers = cart.flowers
#                 flowers.quantity -= cart.quantity
#                 cart.status = 'Оформлен'
#                 flowers.save()
#                 cart.save()
#
#             data = {
#                 'user': payment_user,
#                 'order': order,
#             }
#
#             email_html = render_to_string('email_order.html', data)
#             msg = EmailMultiAlternatives(subject='Уведомление о заказе на сайте FreshCompany', to=[f'{payment_user.email}'])
#             msg.attach_alternative(email_html, 'text/html')
#             msg.send()
#
#             return HttpResponse(status=200)
#
#         else:
#             return HttpResponse(status=200)
#
#     else:
#         return HttpResponse(status=405)

@csrf_exempt
def payment_webhook(request):
    if request.method == 'POST':
        try:
            payment_json = json.loads(request.body)
        except json.JSONDecodeError:
            return HttpResponse(status=400)

        payment_object = payment_json.get('object')
        if not payment_object:
            return HttpResponse(status=400)

        payment_id = payment_object.get('id')
        print(f'Payment_id: {payment_id}')

        payment_status = payment_object.get('status')
        print(f'Payment_status: {payment_status}')

        if payment_status == 'succeeded':
            user_id = int(payment_object['metadata']['user_id'])
            user = User.objects.get(id=user_id)
            print(f'User_id: {user_id} User: {user.username}')

            address = payment_object['metadata'].get('address', '')
            print(f'address {address}')
            taking = payment_object['metadata'].get('taking', '')
            print(f'takibg {taking}')
            summa = payment_object['amount'].get('value', 0)
            print(f'summa {summa}')

            quantity = payment_object['metadata'].get('quantity', 0)
            print(f'quantity {quantity}')
            payment = payment_object['metadata'].get('payment')
            print(f'payment {payment}')

            order = Order.objects.create(
                user=user,
                address=address,
                taking=taking,
                summa=summa,
                taking_summa=500,
                quantity=quantity,
                is_payment=True,
                payment=payment,
                status_payment='Оплачен'
            )

            cart_items = Cart.objects.filter(user=user, status='В корзине')
            order.cart.add(*cart_items)
            order.save()
            print(f'Order: {order}')

            PaymentConnectionOrder.objects.create(payment_id=payment_id, order=order.id)

            for cart in order.cart.all():
                flowers = cart.flowers
                flowers.quantity -= cart.quantity
                cart.status = 'Оформлен'
                flowers.save()
                cart.save()

            data = {
                'user': user,
                'order': order,
            }

            email_html = render_to_string('email_order.html', data)
            msg = EmailMultiAlternatives(
                subject='Уведомление о заказе на сайте FreshCompany',
                to=[user.email]
            )
            msg.attach_alternative(email_html, 'text/html')
            msg.send()
            return HttpResponse(status=200)

        else:
            return HttpResponse(status=200)

    else:
        return HttpResponse(status=405)