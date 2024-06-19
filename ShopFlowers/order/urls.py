from django.urls import path, reverse_lazy
import order.views as order


urlpatterns = [
    path('make_order/', order.MakeOrderView.as_view(), name='make-order'),
    path('order_profile/', order.OrderProfileView.as_view(), name='order-profile'),
    # path('remove_cart/<int:cart_id>/', cart.RemoveCartView.as_view(), name='remove-cart'),
    # path('change_cart/<int:cart_id>/', cart.ChangeCartView.as_view(), name='change-cart'),
]