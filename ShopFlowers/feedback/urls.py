from django.urls import path, reverse_lazy
import feedback.views as feedback


urlpatterns = [
    path('feedback_profile/', feedback.FeedbackProfileView.as_view(), name='feedback-profile'),
    # path('add_cart/<int:product_id>/', cart.AddCartView.as_view(), name='add-cart'),
    # path('remove_cart/<int:cart_id>/', cart.RemoveCartView.as_view(), name='remove-cart'),
    # path('change_cart/<int:cart_id>/', cart.ChangeCartView.as_view(), name='change-cart'),
]