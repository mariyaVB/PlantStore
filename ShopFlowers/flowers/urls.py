from django.urls import path, re_path
import flowers.views as flowers

urlpatterns = [
    path('', flowers.show_main_page),
    path('flowers/', flowers.show_flowers),
    path('error/', flowers.qwerty),
]
