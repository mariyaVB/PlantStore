import os
import json
from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from dotenv import load_dotenv
from yookassa import Payment, Configuration
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


def create_payment(summa, order, user):
    """ Создание оплаты """
    metadata = {
        "user_id": user,
        "order_id": order,
    }
    idempotence_key = str(uuid.uuid4())

    payment = Payment.create({
        "amount": {
            "value": summa,
            "currency": "RUB"
        },
        "confirmation": {
            "type": "redirect",
            "return_url": "https://d4ee-95-58-138-130.ngrok-free.app/order/order_profile/"
        },
        "capture": True,
        "description": "Оплата на сайте FreshCompany",
        "metadata": metadata,
        "test": True,
    }, idempotence_key)
    return payment


@csrf_exempt
def payment_webhook(request):
    if request.method == 'POST':
        try:
            payment_json = json.loads(request.body)
        except json.JSONDecodeError:
            return HttpResponse(status=400)

        payment_object = payment_json['object']
        payment_id = payment_object['id']
        print(f"Payment id: {payment_id}")
        payment_status = payment_object['status']
        print(f"Payment status: {payment_status}")
        order_id = int(payment_object['metadata']['order_id'])
        print(f"Order id: {order_id} and type: {type(order_id)}")
        # payment_order = get_object_or_404(Order, id=order_id)
        payment_order = Order.objects.get(id=order_id)
        print(f'Hz {payment_order}')
        payment_order2 = Order.objects.get(id=92)
        print(f'Hz2 {payment_order2}')
        user_id = int(payment_object['metadata']['user_id'])
        print(f"User id: {user_id} and type: {type(user_id)}")
        payment_user = get_object_or_404(User, id=user_id)
        print(payment_user)
        # payment_user = User.objects.get(id=user_id)

        if payment_status == 'succeeded':
            PaymentConnectionOrder.objects.create(payment_id=payment_id, order=payment_order)
            payment_order.is_payment = True
            payment_order.status_payment = 'Оплачен'
            payment_order.save()
            for cart in payment_order.cart.all():
                flowers = cart.flowers
                flowers.quantity -= cart.quantity
                cart.status = 'Оформлен'
                flowers.save()
                cart.save()
            data = {
                'user': payment_user,
                'order': payment_order,
            }

            email_html = render_to_string('email_order.html', data)
            msg = EmailMultiAlternatives(subject='Уведомление о заказе на сайте FreshCompany', to=[f'{payment_user.email}'])
            msg.attach_alternative(email_html, 'text/html')
            msg.send()
            return HttpResponse(status=200)

        elif payment_status in ['pending', 'canceled']:
            payment_order.delete()
            return HttpResponse(status=200)

        else:
            pass

    else:
        return HttpResponse(status=405)


