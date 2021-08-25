from django.db.models.query import QuerySet
from django.http import request
from django.http.response import Http404
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404, render

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


class ProductFeaturedListView(ListView):
    template_name = "products/featured-product.html"
    
    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.featured()


class ProductDetailSlugView(DetailView):
    queryset = Product.objects.all()
    template_name = "products/featured-product.html"

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        # instance = get_object_or_404(Product, slug=slug)
        try:
            instance = Product.objects.get(slug=slug)
        except Product.DoesNotExist:
            raise Http404("Not found")
        except Product.MultipleObjectsReturned:
            qs = Product.objects.filter(slug=slug)
            instance = qs.first()
        except:
            raise Http404('Nooooo')
        return instance
    

class ProductFeaturedDetailView(DetailView):
    
    template_name = "products/featured-product-detail.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.featured()
