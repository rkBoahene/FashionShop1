import random
import os
from django.db import models
from django.db.models import Q
from django.db.models.signals import pre_save
from django.urls import reverse
from .utils import unique_slug_generator

def get_file_name(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance, filename):
    new_filename = random.randint(1, 33222465)
    name, ext = get_file_name(filename)
    final_filename = '{new_filename}.{ext}'.format(new_filename=name,ext=ext)
    return "products/{new_filename}/{final_filename}".format(new_filename=new_filename,final_filename=final_filename)

# create custom queryset for featured product
class ProductQueryset(models.query.QuerySet):
    def featured(self):
        return self.filter(featured=True)


# create model manager to extend default 'objects call on model query
class ProductManager(models.Manager):
    # override queryset with custom queryset
    def get_queryset(self):
        return ProductQueryset(self.model, using=self.db)

    def features(self,id):
        return self.get_queryset().featured()
    
    # define model manager here
    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()

        return None 

    def search(self, query):
        lookup = Q(title__icontains=query) | Q(description__icontains=query)
        return self.get_queryset().active().filter(lookup).distinct()  

# Create your models here.
class Product(models.Model):
    title = models.CharField( max_length=150)
    slug = models.SlugField(default='bolo',unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    featured = models.BooleanField(default=False)

    # use product manager for objects
    objects = ProductManager()

    def get_absolute_url(self):
        return reverse("products:product-detail", kwargs={"slug": self.slug})
    

    def __str__(self):
        return self.title
    
def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_receiver, sender=Product)