from django.shortcuts import redirect, render
from .models import Cart
from products.models import Product
# Create your views here.


def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    
    return render(request, "cart/home.html")


def cart_update(request):
    product_id = 1
    product_obj = Product.objects.get(id=product_id)
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    cart_obj.products.add(product_obj)
    return redirect(product_obj.get_absolute_url())