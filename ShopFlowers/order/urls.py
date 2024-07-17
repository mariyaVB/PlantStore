from django.urls import path
import order.views as order

app_name = 'order'
urlpatterns = [
    path('add_order/', order.AddOrderView.as_view(), name='add-order'),
    path('order_profile/', order.OrderProfileView.as_view(), name='order-profile'),
    path('order/order-filter/', order.OrderFilter.as_view(), name='order-filter'),
    path('cancel_order/<int:order_id>/', order.CancelOrderView.as_view(), name='cancel-order'),
]
