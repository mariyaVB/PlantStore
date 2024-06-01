from django.urls import path
import users.views as users

urlpatterns = [
    path('login/', users.LoginUser.as_view(), name='login'),
    path('logout/', users.LogoutView.as_view(), name='logout'),
    path('register/', users.RegisterUser.as_view(), name='register'),
    path('profile/', users.ProfileUser.as_view(), name='profile'),
]


