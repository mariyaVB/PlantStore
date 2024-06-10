from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from ShopFlowers import settings
from users.forms import LoginUserForm, RegisterUserForm, ProfileUserForm, PasswordChangeUserForm
from django.http import Http404


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'
    extra_context = {'title': 'Авторизация', 'form_auth': form_class}

    def get_success_url(self):
        return reverse_lazy('main')


class LogoutUser(LogoutView):
    next_page = reverse_lazy('main')


class RegisterUser(CreateView):
    try:
        form_class = RegisterUserForm
        template_name = 'register.html'
        extra_context = {'title': 'Регистрация', 'form_register': form_class}
    except:
        raise Http404('Not Found')

    def get_success_url(self):
        return reverse_lazy('login')


class ProfileUser(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = ProfileUserForm
    template_name = 'profile.html'
    extra_context = {'title': 'Личный кабинет',
                     'default_image': settings.DEFAULT_USER_IMAGE}

    def get_success_url(self):
        return reverse_lazy('profile')

    def get_object(self, queryset=None):
        return self.request.user


class PasswordChangeUser(PasswordChangeView):
    form_class = PasswordChangeUserForm
    template_name = 'password_change_form.html'
    extra_context = {'title': 'Изменение пароля'}

    def get_success_url(self):
        return reverse_lazy('password_change_done')



