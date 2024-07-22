from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('services/', TemplateView.as_view(template_name='services.html'), name='services'),
    path('', include('flowers.urls')),
    path('users/', include('users.urls')),
    path('cart/', include('cart.urls')),
    path('order/', include('order.urls')),
    path('feedback/', include('feedback.urls')),
    path('payment/', include('payment.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = 'ShopFlowers.views.error_404'

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
