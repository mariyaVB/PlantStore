import os
import uuid
import json
import datetime
from django.views.generic import TemplateView
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.db import transaction, IntegrityError
from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from dotenv import load_dotenv
from yookassa import Payment, Refund, Configuration
from cart.models import Cart
from payment.models import PaymentConnectionOrder
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from order.models import Order
from users.models import User
import logging


load_dotenv()
# Configuration.account_id = os.getenv('DJANGO_YOOKASSA_SHOP_ID')
# Configuration.secret_key = os.getenv('DJANGO_YOOKASSA_SECRET_KEY')
Configuration.account_id = '413562'
Configuration.secret_key = 'test_4TVpEYQ4Ebr9Xsa8CR1VO-uacIRXAEMNv2Cw-_SVRMA'
logger = logging.getLogger(__name__)


class PaymentCompletedView(TemplateView):
    template_name = 'payment.html'


def email_client(user, order):
    data = {
        'user': user,
        'order': order,
    }
    try:
        order = Order.objects.get(id=order.id)
    except (ObjectDoesNotExist, TypeError):
        return Http404('Нет заказа')

    if order.status_order == 'Создан':
        email_html = render_to_string('email_order.html', data)
        msg = EmailMultiAlternatives(subject='Уведомление о заказе на сайте FreshCompany', to=[user.email])
        msg.attach_alternative(email_html, 'text/html')
        msg.send()
        return HttpResponse(status=200)

    elif order.status_order == 'Отменен':
        email_html = render_to_string('email_cancel_order.html', data)
        msg = EmailMultiAlternatives(subject='Уведомление о отмене заказа на сайте FreshCompany', to=[f'{user.email}'])
        msg.attach_alternative(email_html, 'text/html')
        msg.send()
        return HttpResponse(status=200)


def create_payment(summa, metadata):
    """ Создание оплаты """
    idempotence_key = str(uuid.uuid4())
    try:
        payment = Payment.create({
            "amount": {
                "value": summa,
                "currency": "RUB"
            },
            "confirmation": {
                "type": "redirect",
                "return_url": "https://mariyaVB.pythonanywhere.com/payment/payment_completed/"
            },
            "capture": True,
            "description": "Оплата на сайте FreshCompany",
            "metadata": metadata,
        }, idempotence_key)

        return payment
    except (IntegrityError, ValidationError):
        return Http404('Ошибка при создании оплаты')


def refund_payment(order):
    """Создание возврата"""
    try:
        payment = PaymentConnectionOrder.objects.get(order=order)
    except PaymentConnectionOrder.DoesNotExist:
        return Http404('Не найдена платежка')

    try:
        refund = Refund.create({
            "amount": {
                "value": order.summa,
                "currency": "RUB",
                "description": "Возврат денежных средств за заказ на сайте FreshCompany",
            },
            "payment_id": payment.payment_id
        })
        return refund
    except (IntegrityError, ValidationError):
        return Http404('Ошибка при создании возврата')


@csrf_exempt
def payment_webhook(request):
    if request.method == 'POST':
        try:
            payment_json = json.loads(request.body)
        except json.JSONDecodeError:
            return HttpResponse(status=400)

        payment_event = payment_json.get('event')
        payment_object = payment_json.get('object')

        if not payment_object:
            return HttpResponse(status=400)

        payment_id = payment_object.get('id')
        payment_status = payment_object.get('status')

        if payment_event == 'payment.succeeded':
            if payment_status == 'succeeded':
                user_id = int(payment_object['metadata']['user_id'])
                user = User.objects.get(id=user_id)
                taking = payment_object['metadata'].get('taking')
                address = payment_object['metadata'].get('address')
                taking_summa = int(payment_object['metadata'].get('taking_summa'))
                summa = float(payment_object['amount'].get('value'))
                quantity = int(payment_object['metadata'].get('quantity'))
                payment = payment_object['metadata'].get('payment')

                order = Order.objects.create(
                    user=user,
                    taking=taking,
                    address=address,
                    taking_summa=taking_summa,
                    quantity=quantity,
                    summa=summa,
                    payment=payment,
                    is_payment=True,
                    status_payment='Оплачен'
                )

                cart_items = Cart.objects.filter(user=user, status='В корзине')
                order.cart.add(*cart_items)
                order.save()
                PaymentConnectionOrder.objects.create(payment_id=payment_id, order=order)

                for cart in order.cart.all():
                    flowers = cart.flowers
                    flowers.quantity -= cart.quantity
                    cart.status = 'Оформлен'
                    flowers.save()
                    cart.save()

                email_client(user, order)
                return HttpResponse(status=200)
            else:
                return Http404()

        elif payment_event == 'refund.succeeded':
            if payment_status == 'succeeded':
                refund_id = payment_object.get('payment_id')
                payment_connection_order = PaymentConnectionOrder.objects.get(payment_id=refund_id)
                order = payment_connection_order.order
                user = order.user

                order.status_order = 'Отменен'
                order.ending_order = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                order.save()
                for cart in order.cart.all():
                    flowers = cart.flowers
                    flowers.quantity += cart.quantity
                    flowers.save()

                email_client(user, order)
                return HttpResponse(status=200)

            else:
                return HttpResponse(status=200)

        else:
            return HttpResponse(status=200)

    else:
        return HttpResponse(status=405)
