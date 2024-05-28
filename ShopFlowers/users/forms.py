from django import forms
from django.contrib.auth.forms import AuthenticationForm


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(max_length=50,
                               widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'введите логин'}))
    password = forms.CharField(max_length=50,
                               widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'введите пароль'}))