import datetime
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm, PasswordResetForm, \
    SetPasswordForm
from users.models import User


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(max_length=50,
                               widget=forms.TextInput(attrs={'class': 'form-input-auth',
                                                             'placeholder': 'Введите логин или E-mail'}))
    password = forms.CharField(max_length=50,
                               widget=forms.PasswordInput(attrs={'class': 'form-input-auth',
                                                                 'placeholder': 'Введите пароль'}))


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин',
                               widget=forms.TextInput(attrs={'class': 'form-input-reg', 'placeholder': 'Логин'}))
    password1 = forms.CharField(label='Пароль',
                                widget=forms.PasswordInput(attrs={'class': 'form-input-reg', 'placeholder': 'Пароль'}))
    password2 = forms.CharField(label='Повтор пароля',
                                widget=forms.PasswordInput(attrs={'class': 'form-input-reg', 'placeholder': 'Повторите пароль'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            'email': 'E-mail',
        }
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-input-reg', 'placeholder': 'E-mail'}),
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Такой E-mail уже существует!")
        return email


class ProfileUserForm(forms.ModelForm):
    username = forms.CharField(disabled=True, label='Логин', widget=forms.TextInput(attrs={'class': 'form-input-profile'}))
    email = forms.CharField(disabled=True, label='E-mail', widget=forms.TextInput(attrs={'class': 'form-input-profile'}))
    this_year = datetime.date.today().year
    date_birth = forms.DateField(label='День рождения',
                                 widget=forms.SelectDateWidget(years=tuple(range(this_year - 70, this_year - 5)),
                                                               attrs={'class': 'form-date-birth'}))

    class Meta:
        model = get_user_model()
        fields = ['photo', 'username', 'email', 'date_birth', 'first_name', 'last_name']
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-input-profile'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input-profile'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-profile-photo'})
        }


class PasswordChangeUserForm(PasswordChangeForm):
    old_password = forms.CharField(label='Старый пароль',
                                   widget=forms.PasswordInput(attrs={'class': 'form-input-change-password',
                                                                     'placeholder': 'Старый пароль'}))
    new_password1 = forms.CharField(label='Новый пароль',
                                   widget=forms.PasswordInput(attrs={'class': 'form-input-change-password',
                                                                     'placeholder': 'Новый пароль'}))
    new_password2 = forms.CharField(label='Повтор нового пароля',
                                   widget=forms.PasswordInput(attrs={'class': 'form-input-change-password',
                                                                     'placeholder': 'Повтор нового пароля'}))


class PasswordResetUserForm(PasswordResetForm):
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-input-reset-password',
                                                                            'placeholder': 'Введите Email',
                                                                            }))


class SetPasswordUserForm(SetPasswordForm):
    new_password1 = forms.CharField(label='Новый пароль',
                                    widget=forms.PasswordInput(attrs={'class': 'form-input-set-password',
                                                                      'placeholder': 'Введите новый пароль',
                                                                      }))

    new_password2 = forms.CharField(label='Подтверждение нового пароля',
                                    widget=forms.PasswordInput(attrs={'class': 'form-input-set-password',
                                                                      'placeholder': 'Подтвердите новый пароль',
                                                                      }))





