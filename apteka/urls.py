"""apteka URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from main.views import index, products, about_us, contacts, cart, shop_single, sendContact, product, addToCart, update_cart, del_product, checkout, addOrder, search, author


urlpatterns = [
    path('', index, name='index'),
    path('products', products, name='products'),
    path('about-us', about_us, name='about-us'),
    path('contacts', contacts, name='contacts'),
    path('cart', cart, name='cart'),
    path('shop-single', shop_single, name='shop-single'),
    path('product/<int:pk>', product, name='product'),
    path('sendContact/', sendContact, name='sendContact'),
    path('addToCart/<int:pk>', addToCart, name='addToCart'),
    path('update_cart/', update_cart, name='update_cart'),
    path('del-product/<int:pk>', del_product, name='del_product'),
    path('checkout', checkout, name='checkout'),
    path('addOrder/', addOrder, name='addOrder'),
    path('search/', search, name='search'),
    path('author/', author, name='author'),
    path('admin/', admin.site.urls),
]



# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)