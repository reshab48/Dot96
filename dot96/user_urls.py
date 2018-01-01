from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^', include('shop.urls', namespace='shop')),
    url(r'^cart/', include('cart.urls', namespace='cart')),
    url(r'^account/', include('account.urls', namespace='account')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)