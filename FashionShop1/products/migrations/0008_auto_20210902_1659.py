# Generated by Django 3.1 on 2021-09-02 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_product_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='flash_sale',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='flash_sale_price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
    ]
