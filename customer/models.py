from django.db import models
from . import models
from  seller .models import *


# Create your models here.

class CustomerRegistration(models.Model):
    name = models.CharField(max_length = 200)
    email = models.EmailField()
    password = models.CharField(max_length = 200)

    def __str__(self):
        return self.name

class Cart(models.Model):
      customer=models.ForeignKey(CustomerRegistration,on_delete=models.CASCADE,null=True)
      product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
      quantity=models.PositiveIntegerField(default=1)