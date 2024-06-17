from django import forms
from django.contrib.auth import get_user_model
from django.http import request

from order.models import Customer, Order
from users.models import User


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'phone', 'address', 'taking']

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-input-order', 'placeholder': 'Имя'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input-order', 'placeholder': 'Фамилия'}),
            'phone': forms.TextInput(attrs={'class': 'form-input-order', 'placeholder': 'Номер телефона'}),
            'address': forms.TextInput(attrs={'class': 'form-input-order', 'placeholder': 'Адрес'}),
            'taking': forms.widgets.Select(attrs={'class': 'form-choice-order',  'id': 'input-delivery'})
        }

