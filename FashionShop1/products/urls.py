from django.urls import path
from .views import (
                    ProductListView, 
                    ProductDetailSlugView,
                    )

app_name='products'

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('details/<slug>', ProductDetailSlugView.as_view(), name='product-detail'),
    # path('details/<int:pk>', ProductDetailView.as_view(), name='product-detail'),
    # path('featured/', ProductFeaturedListView.as_view(), name='index'),
    # path('featured-detail/<int:id>', ProductFeaturedDetailView.as_view(), name='index'),

]
