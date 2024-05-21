from django.urls import path, re_path
import flowers.views as flowers

urlpatterns = [
    path('', flowers.MainPage.as_view(), name='main'),
    path('flowers/', flowers.FlowersView.as_view(), name='flowers'),
    path('flowers/<slug:slug>/', flowers.FlowerDetailView.as_view(), name='flower'),
    path('flowers/categories/<slug:slug>/', flowers.CategoryView.as_view(), name='categories'),
]
