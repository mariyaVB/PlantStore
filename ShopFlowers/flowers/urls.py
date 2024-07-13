from django.urls import path
import flowers.views as flowers

app_name = 'flowers'
urlpatterns = [
    # path('', flowers.MainPage.as_view(), name='main'),
    path('', flowers.plant_news_view, name='main'),
    path('flowers/', flowers.FlowersView.as_view(), name='flowers'),
    path('pots/', flowers.PotsView.as_view(), name='pots'),
    path('care/', flowers.CareView.as_view(), name='care'),
    path('filter-flowers/', flowers.FilterFlowersView.as_view(), name='filter-flowers'),
    path('filter-cares/', flowers.FilterCaresView.as_view(), name='filter-cares'),
    path('filter-pots/', flowers.FilterPotsView.as_view(), name='filter-pots'),
    path('search/', flowers.Search.as_view(), name='search'),
    path('flowers/<slug:slug>/', flowers.FlowerDetailView.as_view(), name='flower'),
]

