from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField( max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.title
    