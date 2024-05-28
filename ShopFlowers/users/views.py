from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy

from users.forms import LoginUserForm


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'
    extra_context = {'title': "Авторизация", 'form_auth': form_class}

    def get_success_url(self):
        return reverse_lazy('main')


class LogoutUser(LogoutView):
    next_page = reverse_lazy('main')

