from django.urls import path
import flowers.views as flowers


urlpatterns = [
    path('', flowers.MainPage.as_view(), name='main'),
    path('flowers/', flowers.FlowersView.as_view(), name='flowers'),
    path('pots/', flowers.PotsView.as_view(), name='pots'),
    path('filter_flowers/', flowers.filter_flowers, name='filter'),
    # path('filter/', flowers.FilterFlowersView.as_view(), name='filter'),
    path('flowers/<slug:slug>/', flowers.FlowerDetailView.as_view(), name='flower'),
    path('flowers/categories/<slug:slug>/', flowers.CategoryView.as_view(), name='categories'),
]

