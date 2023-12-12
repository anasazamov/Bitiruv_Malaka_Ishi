from django.db import models
from django.utils import timezone
from md5_hash import sha256_hash

# Create your models here.

class Category(models.Model):

    pass


class Product(models.Model):

    name = models.CharField(max_length=30)
    product_seria_num = models.CharField(max_length=32,unique=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    end_date = models.DateField()
    utilized = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        # Agar product_seria_num bo'sh bo'lsa, uni to'ldirish
        if not self.product_seria_num:
            self.product_seria_num = sha256_hash(f"{int(timezone.now().timestamp())}".encode('utf-8'))
        super().save(*args, **kwargs)

    def __str__(self)->str:

        return f'Name: {self.name} ID: {self.pk}'