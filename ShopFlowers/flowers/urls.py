from django.urls import path, re_path
import flowers.views as flowers

urlpatterns = [
    path('', flowers.MainPage.as_view()),
    path('flowers/', flowers.FlowersView.as_view()),
]
