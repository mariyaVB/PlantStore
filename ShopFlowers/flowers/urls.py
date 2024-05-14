from django.urls import path, re_path
import flowers.views as flowers

urlpatterns = [
    path('', flowers.show_flowers),
]