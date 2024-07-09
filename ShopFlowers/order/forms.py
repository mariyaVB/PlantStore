from django import forms
from django.core.exceptions import ValidationError
from order.models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['address', 'taking', 'taking_summa', 'summa', 'payment']

        widgets = {
            'address': forms.TextInput(attrs={'class': 'form-input-order', 'placeholder': 'Адрес', 'id': 'address-value'}),
            'taking': forms.widgets.Select(attrs={'class': 'form-choice-order', 'id': 'inputDelivery'}),
            'payment': forms.widgets.Select(attrs={'class': 'form-choice-order', 'id': 'inputPayment'}),
        }

    def clean_address(self):
        address = self.cleaned_data['address']
        if address is not None:
            if len(address) > 100:
                self.add_error('address', 'Адрес превышает 100 символов.')
                raise ValidationError('Адрес превышает 100 символов')
            if len(address) < 5:
                self.add_error('address', 'Адрес не может быть меньше 5 символов.')
                raise ValidationError('Адрес не может быть меньше 5 символов')
        else:
            self.add_error('address', 'Пожалуйста, введите адрес.')
        return address





