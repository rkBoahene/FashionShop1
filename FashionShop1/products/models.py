import random
import os
from django.db import models


def get_file_name(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance, filename):
    new_filename = random.randint(1, 33222465)
    name, ext = get_file_name(filename)
    final_filename = '{new_filename}.{ext}'.format(new_filename=name,ext=ext)
    return "products/{new_filename}/{final_filename}".format(new_filename=new_filename,final_filename=final_filename)

# create model manager to extend default 'objects call on model query
class ProductManager(models.Manager):
    # define model manager here
    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()

        return None 

# Create your models here.
class Product(models.Model):
    title = models.CharField( max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)

    # use product manager for objects
    objects = ProductManager()

    def __str__(self):
        return self.title
    