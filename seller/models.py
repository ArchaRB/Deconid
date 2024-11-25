from django.db import models

# Create your models here.
class SellerRegistration(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    password = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length = 100)
    price = models.IntegerField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product',null=True)
    description = models.TextField(default='No description provided')

    def __str__(self):
        return self.name

