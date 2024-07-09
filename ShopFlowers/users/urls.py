from django.contrib.auth.views import PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView
from django.contrib.auth.views import PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import path, reverse_lazy
import users.views as users
from users.forms import PasswordResetUserForm, SetPasswordUserForm

app_name = 'user'
urlpatterns = [
    path('login/', users.LoginUser.as_view(), name='login'),
    path('logout/', users.LogoutView.as_view(), name='logout'),
    path('register/', users.RegisterUser.as_view(), name='register'),
    path('profile/', users.ProfileUser.as_view(), name='profile'),
    path('password-change/', users.PasswordChangeUser.as_view(), name='password-change'),
    path('password-change/done/', PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
         name='password_change_done'),

    path('password-reset/', PasswordResetView.as_view(template_name='password_reset_form.html',
                                                      form_class=PasswordResetUserForm,
                                                      email_template_name='password_reset_email.html',
                                                      success_url=reverse_lazy('user:password_reset_done')),
         name='password_reset'),

    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
         name='password_reset_done'),


    path('password-reset/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html',
                                          form_class=SetPasswordUserForm,
                                          success_url=reverse_lazy('user:password_reset_complete')),
         name='password_reset_confirm'),

    path('password-reset/complete/',
         PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
         name='password_reset_complete'),

]


