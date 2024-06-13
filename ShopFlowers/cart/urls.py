from django.urls import path, reverse_lazy
import cart.views as cart


urlpatterns = [
    path('', cart.CartShow.as_view(), name='cart'),
    path('add_cart/<int:product_id>/', cart.AddCartView.as_view(), name='add-cart'),
    path('remove_cart/<int:cart_id>/', cart.RemoveCartView.as_view(), name='remove-cart'),
    path('change_cart/<int:cart_id>/', cart.ChangeCartView.as_view(), name='change-cart'),
]
