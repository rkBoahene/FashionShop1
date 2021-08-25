from django.http import request
from django.http.response import Http404
from django.views.generic import ListView, DetailView
from django.shortcuts import render

from .models import Product
# Create your views here.

class ProductListView(ListView):
    model = Product
    template_name = "products/index.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView,self).get_context_data(*args,**kwargs)
        return context
    
class ProductDetailView(DetailView):
    model = Product
    template_name = "products/details.html"

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView).get_context_data(**kwargs)
        
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        instance = Product.objects.get_by_id(pk)
        if instance is None:
            return Http404("Product does not exist")
        return instance

    
def detail(request):
    return render(request,"products/details.html")