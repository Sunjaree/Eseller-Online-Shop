from pyexpat import model
from statistics import mode
from unicodedata import category
from django.db import models
from numpy import ma


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100);
    comment = models.TextField(max_length=100)
    date = models.DateField()
    
    def __str__(self):
        return self.name


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.CharField(max_length=400)
    pub_date = models.DateField()
    image = models.ImageField(upload_to="static")
    

    def __str__(self):
        return self.product_name