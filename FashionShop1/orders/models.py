from django.db import models

from cart.models import Cart

ORDER_STATUS_CHOICES = (
    ('created','Created'),
    ('paid','Paid'),
    ('shipped','Shipped'),
    ('refunded','Refunded')
)


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


# generate order id
# generate order total