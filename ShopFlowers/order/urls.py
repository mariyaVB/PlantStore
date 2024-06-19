from django.urls import path
import order.views as order


urlpatterns = [
    path('add_order/', order.AddOrderView.as_view(), name='add-order'),
    path('order_profile/', order.OrderProfileView.as_view(), name='order-profile'),
    path('cancel_order/<int:order_id>/', order.CancelOrderView.as_view(), name='cancel-order'),
    # path('change_cart/<int:cart_id>/', cart.ChangeCartView.as_view(), name='change-cart'),
]