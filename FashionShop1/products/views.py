from django.views.generic.views import ListView
from django.shortcuts import render

from .models import Product
# Create your views here.

class ProductListView(ListView):
    model = Product
    template_name = "shop/index.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView,self).get_context_data(*args,**kwargs)
        return context
    
