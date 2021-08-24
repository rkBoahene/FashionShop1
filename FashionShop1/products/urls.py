from django.urls import path
from .views import ProductDetailView, ProductListView, detail

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    # path('details/<int:pk>', ProductDetailView.as_view(), name='product-detail')
    path('details/', detail, name='product-detail')
]
