from django.db import models

# Create your models here.

class Category(models.Model):

    pass


class Product(models.Model):

    name = models.CharField(max_length=30)
    product_seria_num = models.CharField(max_length=32)

    price = models.DecimalField(max_digits=10,decimal_places=2)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    end_date = models.DateField()
    utilized = models.BooleanField(default=False)
