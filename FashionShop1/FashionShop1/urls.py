
from os import name
from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf.urls.static import static
from fashionUser.views import about_company, contact_us

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth', include('shop.urls')),
    path('', include('products.urls', namespace='products')),
    path('search/', include('search.urls', namespace='search')),
    path('cart/', include('cart.urls', namespace='cart')),
    # path('cart/', cart_home, name='cart'),
    path('about/',about_company, name='about_company'),
    path('contact/',contact_us, name='contact_us'),
] 


if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)