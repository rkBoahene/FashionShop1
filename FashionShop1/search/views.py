from django.db.models import query

from products.models import Product
from django.shortcuts import render
from django.views.generic.list import ListView

# Create your views here.
class SearchProductView(ListView):
    template_name = "search/view.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        query = request.GET.get('q',None)
        if query is not None:
            return Product.objects.search(query)
        return Product.objects.none()