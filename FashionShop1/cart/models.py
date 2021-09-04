from django.conf import settings
from django.db import models

from products.models import Product

User = settings.AUTH_USER_MODEL

# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) 
    products = models.ManyToManyField(Product, blank=True)
    total = models.DecimalField(default=0.00,max_digits=10, decimal_places=2)
    update = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
    