"""FashionShop1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from os import name
from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf.urls.static import static
from fashionUser.views import about_company, contact_us
from cart.views import cart_home
urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth', include('shop.urls')),
    path('', include('products.urls', namespace='products')),
    path('search/', include('search.urls', namespace='search')),
    path('cart/', cart_home, name='cart'),
    path('about/',about_company, name='about_company'),
    path('contact/',contact_us, name='contact_us'),
] 


if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)