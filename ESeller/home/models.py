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