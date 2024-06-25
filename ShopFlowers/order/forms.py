from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.http import request
from order.models import Customer, Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['address', 'taking', 'taking_summa', 'summa']

        widgets = {
            'address': forms.TextInput(attrs={'class': 'form-input-order', 'placeholder': 'Адрес'}),
            'taking': forms.widgets.Select(attrs={'class': 'form-choice-order', 'id': 'inputDelivery'}),
        }

    def clean_address(self):
        address = self.cleaned_data['address']
        if address is not None:
            if len(address) > 100:
                raise ValidationError('Адрес превышает 100 символов')
            if len(address) < 5:
                raise ValidationError('Адрес не может быть меньше 5 символов')
            return address
        else:
            return address

