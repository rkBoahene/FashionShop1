from django.db import models
from django.db.models.signals import pre_save

from cart.models import Cart
from FashionShop1.utils import unique_order_id_generator
ORDER_STATUS_CHOICES = (
    ('created','Created'),
    ('paid','Paid'),
    ('shipped','Shipped'),
    ('refunded','Refunded')
)

# generate random unique orderID


# Create your models here.
class Order(models.Model):
    order_id = models.CharField( max_length=50, blank=True)
    # billing_profile = 
    # shipping_address =
    # billing_address = 
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, default='created', choices=ORDER_STATUS_CHOICES)
    shipping_total = models.DecimalField(default=6.00 ,max_digits=10, decimal_places=2)
    total = models.DecimalField(default=0.00 ,max_digits=10, decimal_places=2)

    def __str__(self):
        return self.order_id

def pre_save_create_order_id(sender, instance, *args,**kwargs):
    if not instance.order_id:
        instance.order_id = unique_order_id_generator(instance)
    
pre_save.connect(pre_save_create_order_id, sender=Order)


# generate order id
# generate order total